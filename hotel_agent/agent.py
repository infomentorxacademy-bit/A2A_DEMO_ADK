"""STEP 4 - Hotel agent whose tools come from an MCP server (McpToolset).

ADK connects to the MCP server, reads its tool list, and hands those tools to the agent.
You do NOT write the tool functions here - the MCP server owns them.
"""
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StreamableHTTPConnectionParams
from google.adk.models.lite_llm import LiteLlm
load_dotenv()

MODEL = LiteLlm(model="openai/gpt-4o-mini")
MCP_URL = os.getenv("HOTEL_MCP_URL", "http://localhost:8000/mcp")

hotel_tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(url=MCP_URL)
)

root_agent = LlmAgent(
    name="hotel_agent",
    model=MODEL,
    description="Handles hotel, stay and room questions.",
    instruction="You are a hotel assistant. Use the MCP tools to find hotels.",
    tools=[hotel_tools],
)
