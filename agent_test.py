import asyncio
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv()

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

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = create_agent(
        model=llm,
        tools=tools,
    )

    print(f"Loaded {len(tools)} tool(s)")
    print("Agent created")

    response = await agent.ainvoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is 23 plus 19?"
            }
        ]
    }
)

    print(response)


if __name__ == "__main__":
    asyncio.run(main())