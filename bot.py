
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
async def on_message(m):

        if m.content.startswith('-'):
                try:
                        await m.delete(delay=1)
                except Forbidden:
                        print("No permissions to delete file")
                except HTTPException:
                        print("Deleting has failed for unknown reason")
                else:
                        print("One Message Deleted that begins with '-'")




client.run(TOKEN)