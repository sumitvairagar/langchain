import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

def main():
    chat = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="What is LangChain?")
    ]
    
    response = chat.invoke(messages)
    
    print("=" * 50)
    print("LangChain Basic Chat Example")
    print("=" * 50)
    print(f"\nQuestion: {messages[1].content}")
    print(f"\nResponse:\n{response.content}")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
