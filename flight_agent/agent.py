"""STEP 1 - The agent, built directly with ADK's LlmAgent (no LangGraph needed).

LlmAgent runs the whole loop for you:
  question -> LLM decides -> (calls tool) -> tool result -> LLM final answer
"""
import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv
load_dotenv()

MODEL = LiteLlm(model="openai/gpt-4o-mini")


# A TOOL is just a Python function. The docstring + type hints are what the LLM reads
# to understand when and how to call it.
def search_flights(city: str) -> str:
    """Finds flights going to the given city (supports Goa and Mumbai)."""
    flights = {
        "goa": "6E-101 Delhi->Goa 09:00, Rs 5,400",
        "mumbai": "AI-202 Delhi->Mumbai 07:30, Rs 4,100",
    }
    return flights.get(city.lower(), f"No flights found to {city}.")


root_agent = LlmAgent(
    name="flight_agent",
    model=MODEL,
    # 'description' goes into the auto-generated Agent Card (how others discover it)
    description="Handles flight, ticket and airline questions.",
    # 'instruction' is the system prompt (how the agent behaves)
    instruction="You are a flight assistant. Always use the search_flights tool.",
    tools=[search_flights],
)
