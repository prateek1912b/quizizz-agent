import chainlit as cl
import json

from crew import crew

@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="The Creator",
            markdown_description="Create quizizz in seconds with the help of AI!",
            icon='https://quizizz.com/wf/assets/60aca2b71ab9a5018cecf20b_Quizizz_favicon.png',
        ),
    ]
@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"Hello, I am {chat_profile}. Type /start to start the quiz creation process.",
        author=chat_profile,
    ).send()

@cl.on_message
async def main():
    result = json.loads(crew.kickoff())

    print(result)
    print(result['quiz'])

    questions = result['quiz']['questions']

    msg = cl.Message(content="")

    for question in questions:
        msg.stream_token(question)

    await msg.send()
    # await cl.Message(
    #     content=f"The quiz has been created successfully. Here is the quiz:\n\n{result}"
    # ).send()

@cl.on_chat_end
def end():
    print("goodbye", cl.user_session.get("id"))

# import chainlit as cl

# @cl.action_callback("action_button")
# async def on_action(action):
#     await cl.Message(content=f"Executed {action.name}").send()
#     # Optionally remove the action button from the chatbot user interface
#     await action.remove()

# @cl.on_chat_start
# async def start():
#     # Sending an action button within a chatbot message
#     actions = [
#         cl.Action(name="action_button", value="example_value", description="Click me!")
#     ]

#     await cl.Message(content="Interact with this action button:", actions=actions).send()
