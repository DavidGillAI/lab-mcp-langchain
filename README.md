# MCP LangChain Lab

## Overview

This project demonstrates how to integrate the Model Context Protocol (MCP) with LangChain. A custom MCP math server was created exposing both a tool and a resource. LangChain connects to the MCP server, loads the available tools and resources, and creates an agent capable of using them to answer questions.

## Features

* Custom MCP server built with FastMCP
* MCP tool for integer addition
* MCP resource providing server information
* LangChain integration using MultiServerMCPClient
* OpenAI-powered agent using MCP tools
* Resource-aware prompting using MCP resource content

## Project Structure

* `math_server.py` – MCP server exposing the add tool and server information resource
* `test_mcp_connection.py` – Simple MCP connectivity and tool-loading test
* `agent_test.py` – Main demonstration script showing MCP tools, resources, and agent interaction
* `mcp_langchain.ipynb` – Development notebook used during setup and experimentation
* `lab_summary.md` – Lab findings and reflections
* `README.md` – Project documentation

## Setup

1. Create and activate a virtual environment.
2. Install required dependencies.
3. Add your OpenAI API key to a `.env` file.
4. Run the test scripts.

## Usage

Test MCP connectivity:

```bash
python test_mcp_connection.py
```

Run the MCP-enabled agent:

```bash
python agent_test.py
```

## Example

The agent can:

* Read MCP resource information
* Use the MCP add tool
* Answer questions using both tool output and resource context

Example query:

```text
Explain what this MCP server can do, then calculate 23 plus 19.
```

Example result:

```text
This MCP server performs mathematical calculations using an add tool.
The sum of 23 plus 19 is 42.
```

## Notes

During development, MCP tool loading inside Jupyter Notebook encountered a Windows/IPyKernel subprocess issue (`UnsupportedOperation: fileno`). The final implementation was therefore demonstrated using standalone Python scripts.
