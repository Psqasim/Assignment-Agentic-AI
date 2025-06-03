from agents import (
    Agent,
    AsyncOpenAI,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    function_tool,
)
from agents.run import RunConfig
import os
from dotenv import load_dotenv
import random

# Disable tracing
set_tracing_disabled(disabled=True)

# Load environment variables
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set.")

# Set up Gemini client
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Configure model and runner
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# ✅ Tool 1: Add
@function_tool
async def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

# ✅ Tool 2: Get fake weather
@function_tool
async def get_weather(city: str) -> str:
    """Returns fake weather for a given city."""
    temp = random.randint(20, 40)
    condition = random.choice(["Sunny", "Cloudy", "Rainy", "Windy"])
    return f"The weather in {city} is {condition} with {temp}°C."

# ✅ Tool 3: Multiply
@function_tool
async def multiply(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return a * b

# ✅ Tool 4: Greet a person
@function_tool
async def greet(name: str) -> str:
    """Returns a friendly greeting."""
    return f"Hello, {name}! Hope you're having a great day."

# Agent with all tools
agent = Agent(
    name="personal_assistant",
    instructions="You are a helpful assistant. Use ONLY the registered tools to answer questions.",
    tools=[add, get_weather, multiply, greet]
)

# 🔹 Test Examples
result_1 = Runner.run_sync(agent, input="What is 7 + 5?", run_config=config)
print("Addition:", result_1.final_output)

result_2 = Runner.run_sync(agent, input="What's the weather in Lahore?", run_config=config)
print("Weather:", result_2.final_output)

result_3 = Runner.run_sync(agent, input="Multiply 6 and 9", run_config=config)
print("Multiplication:", result_3.final_output)

result_4 = Runner.run_sync(agent, input="Say hello to Qasim", run_config=config)
print("Greeting:", result_4.final_output)
