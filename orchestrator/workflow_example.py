"""STEP 7 - Workflow agents: FIXED order instead of LLM-decided order.

SequentialAgent : A -> B -> C            ParallelAgent : A + B at the same time
LoopAgent       : repeat until done      (workflow agents themselves use no LLM)

NOTE: in ADK an agent instance can have only ONE parent. So each workflow gets its
own fresh RemoteA2aAgent objects (via make_remote_agents) instead of reusing the
ones already attached to the orchestrator.
"""
from google.adk.agents import ParallelAgent, SequentialAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


def make_remote_agents():
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
    return flight, hotel


# Always ask flight, then hotel, in that order
trip_pipeline = SequentialAgent(name="trip_pipeline", sub_agents=list(make_remote_agents()))

# Ask both at the same time (faster when the two don't depend on each other)
trip_parallel = ParallelAgent(name="trip_parallel", sub_agents=list(make_remote_agents()))
