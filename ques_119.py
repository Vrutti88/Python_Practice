# Q119) Write a simple asynchronous function using asyncio that prints a message, waits 1 second, and prints another message.
import asyncio
async def print_messages():
    print("Message 1: Starting the task...")
    await asyncio.sleep(1)  
    print("Message 2: Task completed after 1 second.")
asyncio.run(print_messages())
