"""STEP 2 - Expose the agent over A2A with ONE line.

to_a2a() replaces everything we hand-wrote in the SDK demo:
AgentExecutor + AgentCard + RequestHandler + TaskStore + server app.
The Agent Card is generated automatically from the agent's name/description/tools.

Run from adk_demo/:  uvicorn flight_agent.server:a2a_app --port 9001
"""
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from .agent import root_agent

a2a_app = to_a2a(root_agent, host="localhost", port=9001)  # host/port go into the card URL
