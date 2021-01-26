

import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = ':')


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The QUACK taking over ;-; ")
#Runs when bot is online and active  
  print("BOT IS READY")

client.run(os.environ['DISCORD_TOKEN'])


