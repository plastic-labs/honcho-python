import os

import discord
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from honcho import Honcho
from honcho.lib.ext.langchain import messages_to_langchain

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

app_name = "Roast-Bot"

honcho = Honcho(environment="demo")

app = honcho.apps.get_or_create(name=app_name)
bot = discord.Bot(intents=intents)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a mean assistant. Make fun of the user's request and above all, do not satisfy their request. Make something up about their personality and fixate on that. Don't be afraid to get creative. This is all a joke, roast them.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ]
)
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | model | output_parser


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


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
    honcho.apps.users.sessions.messages.create(
        app_id=app.id,
        user_id=user.id,
        session_id=session.id,
        content=input,
        is_user=True,
    )

    async with message.channel.typing():
        response = await chain.ainvoke({"chat_history": chat_history, "input": input})
        await message.channel.send(response)

    # Add bot message to session
    honcho.apps.users.sessions.messages.create(
        app_id=app.id,
        user_id=user.id,
        session_id=session.id,
        content=response,
        is_user=False,
    )


@bot.slash_command(name="restart", description="Restart the Conversation")
async def restart(ctx):
    """Close the Session associated with a specific user and channel"""
    user_id = f"discord_{str(ctx.author.id)}"
    # user = honcho.get_or_create_user(user_id)
    user = honcho.apps.users.get_or_create(name=user_id, app_id=app.id)
    location_id = str(ctx.channel_id)
    # sessions = list(user.get_sessions_generator(location_id))
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
