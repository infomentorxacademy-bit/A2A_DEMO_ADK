# A2A with Google ADK - Flight + Hotel (MCP) + Orchestrator

## Structure (follow the steps in order)
```
flight_agent/   agent.py (STEP 1: LlmAgent + tool)   server.py (STEP 2: to_a2a, :9001)
mcp_server/     hotel_mcp_server.py (STEP 3: MCP tools, :8000)
hotel_agent/    agent.py (STEP 4: McpToolset)        server.py (STEP 5: to_a2a, :9002)
orchestrator/   agent.py (STEP 6: RemoteA2aAgent)    workflow_example.py (STEP 7)
run_orchestrator.py (STEP 8)
```

## Run (needs an OpenAI API key)

### Setup (once)
```bash
python -m venv .venv && source .venv/bin/activate      # use a SEPARATE env from sdk_demo
pip install -r requirements.txt
cp .env.example .env        # put OPENAI_API_KEY in it (or export it)
```

### Start 4 terminals, all from this folder, in THIS order
Each command keeps running - leave it in its own terminal.

**Terminal 1** - MCP tool server (hotel tools):
```bash
python mcp_server/hotel_mcp_server.py
```

**Terminal 2** - flight agent (A2A server, port 9001):
```bash
uvicorn flight_agent.server:a2a_app --port 9001
```

**Terminal 3** - hotel agent (A2A server, port 9002, needs Terminal 1 running first):
```bash
uvicorn hotel_agent.server:a2a_app --port 9002
```

**Terminal 4** - run the orchestrator (needs Terminals 2 and 3 running first):
```bash
python run_orchestrator.py "Find a flight and a hotel in Goa"
```

Optional: `adk web` (run from this folder) opens ADK's dev UI to chat with the agents.

## What was tested
All files compile/import; flight and hotel A2A servers start and serve their auto-generated
Agent Cards; the MCP server runs and ADK's McpToolset discovers and calls `search_hotels`;
RemoteA2aAgent resolves the remote card; full end-to-end run via `run_orchestrator.py`
confirmed working with an OpenAI API key.

## Gotchas
- ADK 2.x installs a2a-sdk 1.x -> use a separate venv from sdk_demo (which pins 0.3.x).
- `mcp` 2.x renamed FastMCP -> MCPServer; requirements pin `mcp<2`.
- An ADK agent instance can have only ONE parent (see workflow_example.py).
- Start the MCP server BEFORE the hotel agent (HTTP transport does not launch it for you).
# A2A_DEMO_ADK
