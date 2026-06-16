import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["math_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    print(f"Found {len(tools)} tool(s)")
    for tool in tools:
        print(tool.name)


if __name__ == "__main__":
    asyncio.run(main())