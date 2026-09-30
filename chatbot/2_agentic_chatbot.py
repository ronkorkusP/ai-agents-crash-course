import chainlit as cl
import dotenv

dotenv.load_dotenv()

from agents import Runner
from nutrition_agent import nutrition_agent

@cl.on_message
async def on_message(message: cl.Message):
    result = await Runner.run(nutrition_agent, message.content)

    await cl.Message(content=result.final_output).send()