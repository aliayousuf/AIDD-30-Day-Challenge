import os
from dotenv import load_dotenv

from agents import Agent, RunConfig, AsyncOpenAI, Runner, OpenAIChatCompletionsModel

import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent = Agent(
    name="StudyNotesAgent",
    instructions="You are an AI assistant that summarizes PDF content and generates quizzes based on it.",
    model=model,
    tools=[]
)

runner = Runner()

def run_agent(prompt):
    return asyncio.run(runner.run(agent, prompt))
