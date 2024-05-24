import chainlit as cl
from chainlit import run_sync
from langchain.tools import tool

@tool("Ask human about the quiz requirements.")
def get_human_input(question: str) -> str:
    """
        A tool for getting the human input. If you call with a prompt argument, it returns the user input. 
        Take user input only when you need it.
    """
    # Tool logic here
    response = run_sync( cl.AskUserMessage(content=f"{question}").send())
    # prompt = f"\n\033[0;36m{prompt}\033[0m\n"
    if response:
        return response['output']