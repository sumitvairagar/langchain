# Basic Chat Example

A simple demonstration of using LangChain with OpenAI's chat models.

## What This Demonstrates

- Setting up LangChain with OpenAI
- Using environment variables for API keys
- Creating chat messages with system and user roles
- Getting responses from the language model

## How to Run

```bash
# From project root, ensure virtual environment is activated
source venv/bin/activate

# Navigate to this example
cd examples/01_basic_chat

# Run the example
python main.py
```

## Expected Output

```
==================================================
LangChain Basic Chat Example
==================================================

Question: What is LangChain?

Response:
LangChain is a framework for developing applications powered by language models...

==================================================
```

## Screenshot

<img src="../../screenshots/01_basic_chat.png" alt="Basic Chat Output" width="600"/>

## Code Explanation

1. **Load Environment**: Uses `python-dotenv` to load API key from `.env` file
2. **Initialize Chat Model**: Creates a ChatOpenAI instance with GPT-3.5
3. **Create Messages**: Defines system prompt and user question
4. **Get Response**: Invokes the model and displays the result

## Key Concepts

- `ChatOpenAI`: LangChain wrapper for OpenAI's chat models
- `SystemMessage`: Sets the behavior/context for the AI
- `HumanMessage`: Represents user input
- `invoke()`: Sends messages and gets response
