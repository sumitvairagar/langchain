# Agent with Tavily Search Tool

Demonstrates building a LangChain agent that uses Tavily search as a tool to answer questions requiring live web data. Integrated with LangSmith for tracing the agent's reasoning steps.

## What This Demonstrates

- Creating an AI agent with tool-calling capabilities
- Using Tavily search as an external tool
- Agent loop: think → act → observe → repeat
- LangSmith tracing of agent reasoning and tool calls

## How to Run

```bash
# From project root, ensure virtual environment is activated
source venv/bin/activate

# Navigate to this example
cd examples/03_agent_tavily_search

# Run the example
python main.py
```

## Expected Output

```
============================================================
LangChain Agent with Tavily Search Tool
============================================================

Question: What are the latest developments in AI in 2025?

> Entering new AgentExecutor chain...
Invoking: `tavily_search_results_json` with {'query': 'latest AI developments 2025'}
[...search results...]
> Finished chain.

============================================================
Final Answer:
Here are the latest developments in AI in 2025...

============================================================

✓ LangSmith tracing enabled!
View traces at: https://smith.langchain.com
```

## Screenshot

<img src="../../screenshots/03_agent_tavily_search.png" alt="Agent with Tavily Search" width="700"/>

## Setup

1. Get a free Tavily API key at [tavily.com](https://tavily.com)
2. Add to your `.env` file:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## Key Concepts

- **Agent**: An LLM that decides which tools to call and when
- **TavilySearchResults**: A search tool that returns web results
- **AgentExecutor**: Runs the agent loop (reason → tool call → observe → repeat)
- **Tool Calling**: The model generates structured tool calls instead of plain text
- **agent_scratchpad**: Stores intermediate steps (tool calls and results)

## Agent Flow

```
User Question → Agent (LLM) → Decides to search
                    ↓
            Tavily Search Tool → Returns results
                    ↓
            Agent (LLM) → Synthesizes final answer
                    ↓
              LangSmith Tracing
            (logs all steps)
```
