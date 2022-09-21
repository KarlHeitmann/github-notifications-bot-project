# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"message.content={message.content}")
    print(f"message.content.startswith('$hello')={message.content.startswith('$hello')}")
    print(f"message.content.startswith('hello')={message.content.startswith('hello')}")
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('YOUR TOKEN HERE')
