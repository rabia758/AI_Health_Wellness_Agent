from config import HealthWellness
import chainlit as cl
import asyncio
@cl.on_chat_start
async def start():
    await cl.Message(content="welcome To The AI Health Planner Agents AI System. How Can I Help You Today.. ").send()

@cl.on_message
async def main(message: cl.Message):
   user_input = message.content
   response = asyncio.run(HealthWellness(user_input))
   await cl.Message(
        content=f"{response}"
          ).send()


