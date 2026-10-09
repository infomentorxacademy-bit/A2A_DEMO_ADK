"""STEP 8 - Run the orchestrator from code (needs GOOGLE_API_KEY and both A2A servers up).

python run_orchestrator.py "Find a flight and a hotel in Goa"
"""
import asyncio
import sys

from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai import types
from orchestrator.agent import root_agent

load_dotenv()

async def main():
    question = " ".join(sys.argv[1:]) or "Find a flight and a hotel in Goa"
    runner = InMemoryRunner(agent=root_agent, app_name="travel_demo")
    session = await runner.session_service.create_session(app_name="travel_demo", user_id="u1")
    message = types.Content(role="user", parts=[types.Part(text=question)])
    async for event in runner.run_async(user_id="u1", session_id=session.id, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)


asyncio.run(main())
