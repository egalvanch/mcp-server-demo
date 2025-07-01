from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="httpserver", host="0.0.0.0")

@mcp.tool()
def hello(name: str = "World") -> str:
    """Returns a greeting message."""
    return f"Hello, {name} from mcp-new-env!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")