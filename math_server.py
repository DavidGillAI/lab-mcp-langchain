from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math Server")

@mcp.resource("info://server")
def server_info():
    return "This is a simple MCP math server with an add tool."

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()
