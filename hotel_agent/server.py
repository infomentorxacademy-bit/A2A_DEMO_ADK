"""STEP 5 - Expose the hotel agent over A2A.   Run: uvicorn hotel_agent.server:a2a_app --port 9002"""
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from .agent import root_agent

a2a_app = to_a2a(root_agent, host="localhost", port=9002)
