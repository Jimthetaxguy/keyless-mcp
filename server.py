from typing import Annotated
from zeromcp import McpServer

mcp = McpServer(
    "keyless-mcp",
    instructions="A simple keyless MCP server. No authentication required."
)

@mcp.tool
def echo(message: Annotated[str, "Message to echo back"]) -> str:
    """Echo the input message back to the caller."""
    return message

@mcp.tool
def add(a: Annotated[int, "First number"], b: Annotated[int, "Second number"]) -> int:
    """Add two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.serve("0.0.0.0", 8000)