"""STEP 3 - A tiny MCP server that offers hotel tools.

MCP = how an agent gets TOOLS.   A2A = how an agent talks to other AGENTS.
This server must be RUNNING before the hotel agent starts (HTTP transport).

Run:  python mcp_server/hotel_mcp_server.py      -> http://localhost:8000/mcp
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hotel-tools", host="127.0.0.1", port=8000)

HOTELS = {
    "goa": "Sea Breeze Resort, Calangute - Rs 3,200/night",
    "mumbai": "Marine View Inn, Colaba - Rs 4,500/night",
}


@mcp.tool()
def search_hotels(city: str) -> str:
    """Finds hotels in the given city (supports Goa and Mumbai)."""
    return HOTELS.get(city.lower(), f"No hotels found in {city}.")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
