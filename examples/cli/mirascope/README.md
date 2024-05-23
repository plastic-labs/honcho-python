# Simple CLI Chatbot with Mirascope

This is a quick demo that shows how to create a chatbot with MiraScope using
Honcho as the storage engine. 

It uses the command line as an interface and uses GPT-4o as the underlying
model. Follow the below steps to setup the demo. 

1. Install the dependencies with `poetry` 

```bash
poetry shell
poetry install
```

2. Add your OpenAI API key to an `.env` file

```bash
echo "OPENAI_API_KEY=<YOUR_API_KEY>" > .env
```

3. Run the demo from your poetry demo

```bash
poetry shell
python main.py
```
