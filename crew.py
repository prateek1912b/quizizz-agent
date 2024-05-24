import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from langchain_community.chat_models.openai import ChatOpenAI

from tools.human_input import get_human_input

load_dotenv()

analyst = Agent(
    role = 'Quiz Creator', 
    goal = 'Provide the user with a quiz based on the requirements provided by the user.',
    backstory = (
        "You are a quiz creating expert. You have created quizzes for various domains and have a good understanding of the requirements of the user."
        "You have a good understanding of the topics and subjects provided by the user and can create a quiz."
        "You also can infer appropriate reading-level and grade level of the quiz based on the topics provided by the user."
    ),
    # verbose = True,
    allow_delegation = False,
    llm = ChatOpenAI(
        openai_api_key=os.environ.get('OPENAI_API_KEY'), 
        model=os.environ.get('OPENAI_MODEL_NAME')
    ),
    tools = [
        get_human_input
    ]
)

task = Task(
    description = (
         "A teacher wants to create a quiz for their students. Based on the requirements provided by the teacher, create a quiz.\n"
         "The quiz should have a default of 10 questions unless specified otherwise by the teacher.\n"
         "The quiz should be based on the topic and subject provided by the teacher.\n"
         "The reading-level and grade level of the quiz should be based on the topics unless specified otherwise by the teacher.\n"
         "The quiz can be of different types like: multiple choice, true/false, fill in the blanks, open-ended, etc.\n"
    ),
    expected_output="The final quiz which can be used by the teacher for their students.",
    agent=analyst,
)

task2 = Task(
    description = (
        "Based on the quiz created earlier, format the quiz in a JSON format.\n"
        "The JSON format should have the following structure:\n"
    ),
    expected_output="The final quiz which can be used by the teacher for their students.",
    agent=analyst,
)

crew = Crew(
    agents=[analyst],
    tasks=[task, task2],
    verbose=2
)
