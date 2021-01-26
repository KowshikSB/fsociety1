

import os
import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = '^')



#Runs when bot is online and active  
  
@client.command()
async def ping(ctx, arg=None):
  if arg=="Pong":
    await ctx.send("Sexy job you just ponged yourself <a:shiba_Sexy_wink:794199806833590302> ")
  else:
    await ctx.send(f'<:wot:790094440387182604> Pong! `{round(client.latency *1000)}ms`')
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The Ded Chat ;-;"))
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="To KaZE"))
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="QUACK taking over"))
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="F SOCIETY"))
  print("Ready")
async def ch_pr():
  await client.wait_until_ready()
  statuses = [ "The Ded Chat ;-;"]
  while not client.is_closed():
    status=random.choice(statuses)
    await client.change_presence(activity=discord.watching(name=status))
    await asyncio.sleep(10)
client.loop.create_task(ch_pr)

client.run(os.environ['DISCORD_TOKEN'])


