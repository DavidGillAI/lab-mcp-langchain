from mcp.server.fastmcp import FastMCP
# Create MCP server
mcp = FastMCP("Math Server")

# MCP resource providing server information
@mcp.resource("info://server")
def server_info():
    return "This is a simple MCP math server with an add tool."

# MCP tool for addition
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()
