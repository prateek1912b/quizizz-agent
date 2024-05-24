import chainlit as cl
from chainlit import run_sync
from langchain.tools import tool
from crewai_tools import FileReadTool

@tool("Read question type and its structure from the file. File contains sample questions, infer the schema of the question types from the file.")
def get_file_reader(question: str) -> str:
    """
        Read question type and its structure from the file. File contains sample questions, infer the schema of the question types from the file.
    """
    # Tool logic here
    file_read_tool = FileReadTool(file_path='~/Dev2/quizizz-agent/question_types.json')
    # response = run_sync( cl.AskUserMessage(content=f"{question}").send())
    # prompt = f"\n\033[0;36m{prompt}\033[0m\n"
    return file_read_tool
