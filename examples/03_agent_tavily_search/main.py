import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file (API keys, etc.)
load_dotenv()

# LangSmith will automatically trace if LANGCHAIN_TRACING_V2 is set in .env
def main():
    # Step 1: Create the language model
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    # Step 2: Set up Tavily search as a tool
    search_tool = TavilySearchResults(max_results=5)

    # Step 3: Define the agent's prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful research assistant. Use the search tool to find current information. Be concise and well-structured in your responses."),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])

    # Step 4: Create the agent and executor
    agent = create_tool_calling_agent(model, [search_tool], prompt)
    executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

    # Three real-world queries that showcase the agent's capabilities
    queries = [
        "Find 5 AI Engineer jobs in Pune posted this week and summarize the key skills required",
        "What did OpenAI, Google, and Anthropic release in the last 30 days?",
        "What tech conferences are happening in India in the next 3 months?",
    ]

    for i, question in enumerate(queries, 1):
        print("\n" + "=" * 60)
        print(f"🔍 Query {i}/3")
        print("=" * 60)
        print(f"\n💬 {question}\n")

        response = executor.invoke({"input": question})

        print("\n" + "-" * 60)
        print(f"✅ Answer:\n{response['output']}")
        print("=" * 60)

    # LangSmith tracing status
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        print("\n✓ LangSmith tracing enabled!")
        print(f"View traces at: {os.getenv('LANGCHAIN_ENDPOINT', 'https://smith.langchain.com')}")
    else:
        print("\n⚠ LangSmith tracing not enabled. Add LANGCHAIN_TRACING_V2=true to .env")

if __name__ == "__main__":
    main()
