# Chains with LangSmith Tracing

Demonstrates building a simple LangChain chain using LCEL (LangChain Expression Language) and integrating with LangSmith for observability.

## What This Demonstrates

- Creating prompt templates
- Building chains with LCEL (pipe operator)
- Output parsing
- LangSmith integration for tracing and monitoring
- Chain composition: Prompt → Model → Parser

## How to Run

```bash
# From project root, ensure virtual environment is activated
source venv/bin/activate

# Navigate to this example
cd examples/02_chains_langsmith

# Run without LangSmith (basic mode)
python main.py

# Run with LangSmith tracing (requires LangSmith account)
# Add to .env file:
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=your_langsmith_api_key
python main.py
```

## Expected Output

```
============================================================
LangChain Chain with LangSmith Tracing
============================================================

Question: What is a Python decorator?

Response:
A Python decorator is a function that modifies the behavior of another 
function or method. It allows you to wrap another function to extend 
its functionality without permanently modifying it...

============================================================

✓ LangSmith tracing enabled!
View traces at: https://smith.langchain.com
```

## Screenshot

![Chain with LangSmith](../../screenshots/02_chains_langsmith.png)

## LangSmith Setup (Optional)

1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Get your API key from settings
3. Add to `.env`:
   ```
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langsmith_api_key
   ```

## Key Concepts

- **Prompt Template**: Reusable prompt structure with variables
- **LCEL (|)**: Pipe operator chains components together
- **StrOutputParser**: Extracts string content from model response
- **LangSmith**: Observability platform for debugging and monitoring chains
- **Tracing**: Automatic logging of chain execution steps

## Chain Flow

```
User Input → Prompt Template → LLM → Output Parser → Final Response
                                ↓
                          LangSmith Tracing
                        (logs all steps)
```
