import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file (API keys, etc.)
load_dotenv()

# LangSmith will automatically trace if LANGCHAIN_TRACING_V2 is set in .env
def main():
    # Step 1: Create a prompt template
    # This is a reusable template where {question} is a variable that gets filled in later
    # It defines two messages: system (sets AI behavior) and user (the actual question)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding assistant. Explain concepts concisely."),
        ("user", "{question}")  # {question} will be replaced with actual question
    ])
    
    # Step 2: Create the language model
    # ChatOpenAI is a wrapper around OpenAI's chat models (like ChatGPT)
    # temperature=0.7 controls randomness (0=deterministic, 1=creative)
    model = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    # Step 3: Create an output parser
    # The model returns a complex object with metadata (tokens, model info, etc.)
    # StrOutputParser extracts just the text content from the response
    # Without it: AIMessage(content="A decorator is...", response_metadata={...})
    # With it: "A decorator is..."
    output_parser = StrOutputParser()
    
    # Step 4: Chain components together using LCEL (LangChain Expression Language)
    # The | (pipe) operator connects components in sequence:
    # 1. prompt formats the input
    # 2. model generates a response
    # 3. output_parser extracts clean text
    chain = prompt | model | output_parser
    
    # Step 5: Run the chain with actual input
    # Pass a dictionary with values for template variables (question in this case)
    question = "What is a Python decorator?"
    response = chain.invoke({"question": question})
    
    # Display results
    print("=" * 60)
    print("LangChain Chain with LangSmith Tracing")
    print("=" * 60)
    print(f"\nQuestion: {question}")
    print(f"\nResponse:\n{response}")
    print("\n" + "=" * 60)
    
    # Check if LangSmith tracing is enabled
    # LangSmith logs each step of the chain for debugging and monitoring
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        print("\n✓ LangSmith tracing enabled!")
        print(f"View traces at: {os.getenv('LANGCHAIN_ENDPOINT', 'https://smith.langchain.com')}")
    else:
        print("\n⚠ LangSmith tracing not enabled. Add LANGCHAIN_TRACING_V2=true to .env")

if __name__ == "__main__":
    main()
