from langgraph.prebuilt import chat_agent_executor
from langchain_core import tools
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

#importing the .env file
load_dotenv()

#declearing the tool
@tool
def calculator(a: float, b: float) -> str:
    """
    perform basic arithmetic operations and return the result as a formatted string
    
    args:
        a (float): The first number
        b (float): The second number
    
    return:
        str: The result of the operation as a formatted string
    """
    print("--- TOOL CALLED ---")
    addition= a + b
    return f"Addition of {a} and {b} is {addition}"

def main():
    # setting up the groq model
    model = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)
    # setting up the tools
    tools = [calculator]
    # creating the agent executor
    agent_executor = create_react_agent(model, tools)
    # welcoming the user
    print("Welcom! I'm your AI assistant. Type 'quit' to exit")
    print("you can ask me to perform calculation or chat with me.")

    # loop for the user input
    while True:
        # taking the user input
        user_input = input("\nYou: ").strip() 
        # cheaking if the user input is 'quit' to exit the loop
        if user_input == "quit":
            print("bye, thanks for using the assistant.")
            break
        # printing the assistant response
        print("\nAssistant: ",end="")
        # streaming the agent response
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # check the agent message in chunks
            if "agent" in chunk and "messages" in chunk["agent"]:
                # getting the message without changing the line
                for message in chunk["agent"]["messages"]:
                    # printing the message
                    print(message.content, end="")
        # new line after the message
        print()

if __name__ == "__main__":
    main()               
