import os

import discord
from dspy import Example
from graph import chat
from dotenv import load_dotenv

from honcho import Honcho, NotFoundError
from honcho.lib.ext.langchain import messages_to_langchain

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.reactions = True  # Enable reactions intent

app_name = "DSPy-Personas"

honcho = Honcho(environment="demo")

app = honcho.apps.get_or_create(name=app_name)
bot = discord.Bot(intents=intents)

thumbs_up_messages = []
thumbs_down_messages = []


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    """Event that is run when a new member joins the server"""
    await member.send(
        f"*Hello {member.name}, welcome to the server! This is a demo bot built with Honcho,* "
        "*implementing a naive user modeling method.* "
        "*To get started, just type a message in this channel and the bot will respond.* "
        '*Over time, it will classify the "state" you\'re in and optimize conversations based on that state.* '
        "*You can use the /restart command to restart the conversation at any time.* "
        "*If you have any questions or feedback, feel free to ask in the #honcho channel.* "
        "*Enjoy!*"
    )


@bot.event
async def on_message(message):
    """Event that is run when a message is sent in a channel that the bot has access to"""
    if message.author == bot.user:
        # ensure the bot does not reply to itself
        return

    # Get a user object for the message author
    user_id = f"discord_{str(message.author.id)}"
    user = honcho.apps.users.get_or_create(name=user_id, app_id=app.id)

    # Get the session associated with the user and location
    location_id = str(message.channel.id)  # Get the channel id for the message

    sessions = [
        session
        for session in honcho.apps.users.sessions.list(
            user_id=user.id, app_id=app.id, is_active=True, location_id=location_id
        )
    ]

    if len(sessions) > 0:
        session = sessions[0]
    else:
        session = honcho.apps.users.sessions.create(user_id=user.id, app_id=app.id, location_id=location_id)

    history = [
        message
        for message in honcho.apps.users.sessions.messages.list(session_id=session.id, app_id=app.id, user_id=user.id)
    ]
    chat_history = messages_to_langchain(history)

    # Add user message to session
    input = message.content
    user_message = honcho.apps.users.sessions.messages.create(
        app_id=app.id,
        user_id=user.id,
        session_id=session.id,
        content=input,
        is_user=True,
    )

    async with message.channel.typing():
        payload = {
            "app": app,
            "user": user,
            "session": session,
            "message": user_message,
        }
        response = await chat(
            honcho=honcho,
            chat_history=chat_history,
            payload=payload,
            input=input,
        )
        await message.channel.send(response)

    # Add bot message to session
    honcho.apps.users.sessions.messages.create(
        app_id=app.id,
        user_id=user.id,
        session_id=session.id,
        content=response,
        is_user=False,
    )


@bot.event
async def on_reaction_add(reaction, user):
    # Ensure the bot does not react to its own reactions
    if user == bot.user:
        return

    # Get a user object for the message author
    user_id = f"discord_{str(user.id)}"
    user = honcho.apps.users.get_or_create(name=user_id, app_id=app.id)

    # Get the session associated with the user and location
    location_id = str(reaction.message.channel.id)  # Get the channel id for the message

    sessions = [
        session
        for session in honcho.apps.users.sessions.list(
            user_id=user.id, app_id=app.id, is_active=True, location_id=location_id
        )
    ]

    if len(sessions) > 0:
        session = sessions[0]
    else:
        session = honcho.apps.users.sessions.create(user_id=user.id, app_id=app.id, location_id=location_id)

    # messages = list(session.get_messages_generator(reverse=True))
    messages = [
        message
        for message in honcho.apps.users.sessions.messages.list(
            session_id=session.id, app_id=app.id, user_id=user.id, reverse=True
        )
    ]
    ai_responses = [message for message in messages if not message.is_user]
    user_responses = [message for message in messages if message.is_user]
    # most recent AI response
    ai_response = ai_responses[0].content
    user_response = user_responses[0]

    user_state_storage: dict = dict(user.metadata)  # type: ignore
    user_state = [
        mm
        for mm in honcho.apps.users.sessions.metamessages.list(
            session_id=session.id, app_id=app.id, user_id=user.id, reverse=True, metamessage_type="user_state", size=1
        )
    ][0].content
    #     session.get_metamessages_generator(metamessage_type="user_state", message=user_response, reverse=True)
    # )[0].content
    examples = user_state_storage[user_state]["examples"]

    # Check if the reaction is a thumbs up
    if str(reaction.emoji) == "👍":
        example = Example(
            chat_input=user_response.content,
            response=ai_response,
            assessment_dimension=user_state,
            label="yes",
        ).with_inputs("chat_input", "response", "assessment_dimension")
        examples.append(example.toDict())
    # Check if the reaction is a thumbs down
    elif str(reaction.emoji) == "👎":
        example = Example(
            chat_input=user_response.content,
            response=ai_response,
            assessment_dimension=user_state,
            label="no",
        ).with_inputs("chat_input", "response", "assessment_dimension")
        examples.append(example.toDict())

    user_state_storage[user_state]["examples"] = examples
    honcho.apps.users.update(user_id=user.id, app_id=app.id, metadata=user_state_storage)
    # honcho_user.update(metadata=user_state_storage)


@bot.slash_command(name="restart", description="Restart the Conversation")
async def restart(ctx):
    """Close the Session associated with a specific user and channel"""
    user_id = f"discord_{str(ctx.author.id)}"
    user = honcho.apps.users.get_or_create(name=user_id, app_id=app.id)
    location_id = str(ctx.channel_id)
    sessions = [
        session
        for session in honcho.apps.users.sessions.list(
            user_id=user.id, app_id=app.id, is_active=True, location_id=location_id
        )
    ]
    if len(sessions) > 0:
        honcho.apps.users.sessions.delete(app_id=app.id, user_id=user.id, session_id=sessions[0].id)

    msg = "Great! The conversation has been restarted. What would you like to talk about?"
    await ctx.respond(msg)


bot.run(os.environ["BOT_TOKEN"])
