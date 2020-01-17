
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

        for GUILD in client.guilds:
                if GUILD == GUILD.name:
                        break
        print(
                f'\n\n{client.user} is connected to the following GUILD:\n'
                f'{GUILD.name}(id: {GUILD.id})\n'
        )

        members = '\n - '.join([member.name for member in GUILD.members])
        print(f'GUILD Members:\n - {members}')

@client.event
async def on_message(message):
        #Is user message a command?
        if (message.content.startswith("-")):
                await asyncio.sleep(1)
                message.delete
        
        #find Groovy user
        for GUILD in client.guilds:
                if GUILD == GUILD.name:
                        break
        for member in GUILD.members:
                if member.name == "Groovy":
                        groovyUser = member
                        break

        def is_bot(message):
                return message.author == groovyUser
        
        await message.channel.purge(limit=100, check=is_bot)



client.run(TOKEN)