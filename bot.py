
# bot.py
import os

import discord
from dotenv import load_dotenv
import time
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILDID = os.getenv('DISCORD_GUILD_ID')


client = discord.Client()

@client.event
async def on_ready():
        #If connected to my guild
        for GUILD in client.guilds:
                if GUILD == GUILD.name:
                        break
        #prints guild
        print(
                f'\n\n{client.user} is connected to the following GUILD:\n'
                f'{GUILD.name}(id: {GUILD.id})\n'
        )
        #Lists the members in my server
        #members = '\n - '.join([member.name for member in GUILD.members])
        #print(f'GUILD Members:\n - {members}')

@client.event
async def on_message(m):
        print("MESSAGE FROM " + str(m.author))
        radioChannel = "radio-shit"
        radioName = "Groovy"
        commandChar = '-'
        
        #If commandChar and in the wrong channel
        if m.content.startswith(commandChar) and str(m.channel) != radioChannel:
                try:
                        #Delete message (delay=Optional Delay seconds)
                        await m.delete(delay=0)
                except:
                        print("Deleting has failed for unknown reason")
                else:
                        print("Command message deleted")           

        if m.author.name == radioName and str(m.channel) != radioChannel:
                try:
                        await m.delete(delay=0)
                except:
                        print("Deleting failed for unknown reason")
                else:
                        print("Groovy message deleted")





client.run(TOKEN)