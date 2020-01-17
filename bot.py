
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




client.run(TOKEN)