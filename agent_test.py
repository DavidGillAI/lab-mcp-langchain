import asyncio
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv()

# Load MCP resource information
async def test_resources(client):
    resources = await client.get_resources()
    return resources[0].as_string()

# Connect to MCP server
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
# Load available MCP tools
    tools = await client.get_tools()

    llm = ChatOpenAI(model="gpt-4o-mini")
# Create LangChain agent with MCP tools
    agent = create_agent(
        
        model=llm,
        tools=tools,
    )

    print(f"Loaded {len(tools)} tool(s)")
    print("Agent created")
 # Retrieve MCP resource content and use it as context
    resource_text = await test_resources(client)

    print(resource_text)

    response = await agent.ainvoke(
    {
        "messages": [
    {
        "role": "system",
        "content": f"Resource information: {resource_text}"
    },
    {
        "role": "user",
        "content": "Explain what this MCP server can do, then calculate 23 plus 19."
    }
        ]
    }
)

    print(response)


if __name__ == "__main__":
    asyncio.run(main())