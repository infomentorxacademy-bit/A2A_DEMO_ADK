"""STEP 6 - The orchestrator: remote A2A agents become sub_agents.

RemoteA2aAgent = a stand-in for an agent running elsewhere. It fetches the remote
Agent Card and calls it over A2A. The orchestrator's LLM chooses which sub-agent to
delegate to, based on each one's 'description'.

Adding another agent = add one RemoteA2aAgent(...) to the list below.
"""
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

MODEL = LiteLlm(model=os.getenv("ADK_MODEL", "openai/gpt-4o-mini"))

flight = RemoteA2aAgent(
    name="flight_agent",
    description="Handles flight, ticket and airline questions.",
    agent_card="http://localhost:9001/.well-known/agent-card.json",
)

hotel = RemoteA2aAgent(
    name="hotel_agent",
    description="Handles hotel, stay and room questions.",
    agent_card="http://localhost:9002/.well-known/agent-card.json",
)

root_agent = LlmAgent(
    name="orchestrator",
    model=MODEL,
    instruction=(
        "You are a travel orchestrator. Delegate flight questions to flight_agent and "
        "hotel questions to hotel_agent. Combine their answers for the user."
    ),
    sub_agents=[flight, hotel],
)
