import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env file (API keys, etc.)
load_dotenv()


# Step 1: Define Pydantic models for structured output
# Instead of getting free-form text, we force the LLM to return data
# that matches these exact schemas — making it easy to use programmatically
class JobListing(BaseModel):
    """A single job listing."""
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    skills: list[str] = Field(description="Key skills required")


class JobSearchResult(BaseModel):
    """Structured result for a job search query."""
    jobs: list[JobListing] = Field(description="List of job listings found")
    top_skills: list[str] = Field(description="Most common skills across all listings")


class AIRelease(BaseModel):
    """A single AI product release."""
    company: str = Field(description="Company name")
    product: str = Field(description="Product or model name")
    summary: str = Field(description="One-line summary of the release")


class AIReleasesResult(BaseModel):
    """Structured result for AI releases query."""
    releases: list[AIRelease] = Field(description="List of recent releases")


def run_agent_query(agent, question: str) -> str:
    """Run the agent and return the raw text response."""
    result = agent.invoke({"messages": [("user", question)]})
    # Get the last AI message content
    return result["messages"][-1].content


def run_structured_query(model, raw_answer: str, schema: type[BaseModel]) -> dict:
    """Take raw agent text and parse it into structured data.

    with_structured_output() forces the LLM to return JSON matching
    the Pydantic schema — no regex parsing or string manipulation needed.
    """
    structured_model = model.with_structured_output(schema)
    result = structured_model.invoke(
        f"Extract structured data from this text:\n\n{raw_answer}"
    )
    return result if isinstance(result, dict) else result.model_dump()


def main():
    # Step 2: Set up the agent using LangGraph's create_react_agent
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    search_tool = TavilySearchResults(max_results=5)

    # create_react_agent builds a ReAct agent that reasons and acts in a loop
    agent = create_react_agent(model, [search_tool])

    # ── Query 1: Job Search → Structured ──
    print("\n" + "=" * 60)
    print("🔍 Query 1: Job Search (Structured Output)")
    print("=" * 60)

    question1 = "Find 5 AI Engineer jobs in Pune posted this week with required skills"
    print(f"\n💬 {question1}\n")

    raw_answer1 = run_agent_query(agent, question1)
    structured1 = run_structured_query(model, raw_answer1, JobSearchResult)

    print("✅ Raw Answer (unstructured text):")
    print(raw_answer1[:300] + "...\n")
    print("📦 Structured Output (Pydantic → JSON):")
    print(json.dumps(structured1, indent=2))

    # ── Query 2: AI Releases → Structured ──
    print("\n" + "=" * 60)
    print("🔍 Query 2: AI Releases (Structured Output)")
    print("=" * 60)

    question2 = "What did OpenAI, Google, and Anthropic release in the last 30 days?"
    print(f"\n💬 {question2}\n")

    raw_answer2 = run_agent_query(agent, question2)
    structured2 = run_structured_query(model, raw_answer2, AIReleasesResult)

    print("✅ Raw Answer (unstructured text):")
    print(raw_answer2[:300] + "...\n")
    print("📦 Structured Output (Pydantic → JSON):")
    print(json.dumps(structured2, indent=2))

    # ── Show the difference ──
    print("\n" + "=" * 60)
    print("💡 Why Structured Output Matters")
    print("=" * 60)
    print(f"\nJobs found: {len(structured1['jobs'])}")
    print(f"Top skills across all listings: {', '.join(structured1['top_skills'])}")
    print(f"\nAI releases found: {len(structured2['releases'])}")
    for r in structured2["releases"]:
        print(f"  • {r['company']}: {r['product']} — {r['summary']}")

    # LangSmith tracing status
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        print(f"\n✓ LangSmith tracing enabled!")
        print(f"View traces at: {os.getenv('LANGCHAIN_ENDPOINT', 'https://smith.langchain.com')}")


if __name__ == "__main__":
    main()
