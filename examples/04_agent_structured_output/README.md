# Agent with Structured Output

Builds on [Example 03](../03_agent_tavily_search/) by adding Pydantic models to parse the agent's free-form text into clean, typed JSON — making LLM responses usable in real applications.

## What This Demonstrates

- Defining Pydantic models as output schemas
- Using `with_structured_output()` to force LLM responses into a schema
- Comparing raw text vs structured JSON output
- Two-step pattern: Agent searches → LLM structures the result

## How to Run

```bash
# From project root, ensure virtual environment is activated
source venv/bin/activate

# Navigate to this example
cd examples/04_agent_structured_output

# Run the example
python main.py
```

## Expected Output

```
============================================================
🔍 Query 1: Job Search (Structured Output)
============================================================

💬 Find 5 AI Engineer jobs in Pune posted this week with required skills

> Entering new AgentExecutor chain...
Invoking: `tavily_search_results_json` with {'query': '...'}
> Finished chain.

------------------------------------------------------------
✅ Raw Answer (unstructured text):
I found 5 AI Engineer jobs in Pune posted this week...

📦 Structured Output (Pydantic → JSON):
{
  "jobs": [
    {
      "title": "AI Lead Engineer",
      "company": "EY",
      "skills": ["Python", "LLM", "RAG", "Tensorflow"]
    },
    ...
  ],
  "top_skills": ["Python", "LLM", "GenAI", "Kubernetes"]
}

💡 Why Structured Output Matters
Jobs found: 5
Top skills across all listings: Python, LLM, GenAI, Kubernetes
```

## Screenshot

<img src="../../screenshots/04_agent_structured_output.png" alt="Agent with Structured Output" width="700"/>

## Key Concepts

- **Pydantic Models**: Define the exact shape of data you want back from the LLM
- **`with_structured_output()`**: Forces the LLM to return JSON matching your schema
- **Two-step pattern**: Agent gets raw info → second LLM call structures it
- **Why it matters**: Raw text is hard to use in code. Structured output gives you typed objects you can iterate, filter, store in a DB, or send via API

## Flow

```
User Question → Agent + Tavily Search → Raw Text Answer
                                              ↓
                              with_structured_output(Pydantic)
                                              ↓
                                    Clean JSON / Python Object
```
