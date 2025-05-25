import os
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
)
from dotenv import load_dotenv

# Load .env and API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Initialize client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Message list with proper typing
messages: list[
    ChatCompletionSystemMessageParam
    | ChatCompletionUserMessageParam
    | ChatCompletionAssistantMessageParam
] = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🔵 Ask me anything! Type 'exit' to quit.\n")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="google/gemma-3-12b-it:free",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("🤖 Bot:", reply)

    messages.append({"role": "assistant", "content": reply})
