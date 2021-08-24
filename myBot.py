import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client() # instance of client - connects to discord
TOKEN = os.getenv('BOT_TOKEN')

@client.event # registers an event. uses callbacks (function called when something else happens)
async def on_ready(): # called when bot ready to start being used
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message): # called when bot receives a woman
    if message.author == client.user: # we dont want anything to happen if the message is from ourselves (i.e. the bot)
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if 'computer' in message.content.lower():
        await message.channel.send('I agree')

client.run(TOKEN) # runs bot with log in token
