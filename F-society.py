

import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '^')


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="QUACK taking over"))
#Runs when bot is online and active  
  print("BOT IS READY")
@client.command()
async def ping(ctx, arg=None):
  if arg=="Pong":
    await ctx.send("Sexy job you just ponged yourself <a:shiba_Sexy_wink:794199806833590302> ")
  else:
    await ctx.send(f'<:wot:790094440387182604> Pong! {round(client.latency *1000)}ms')
@client.event()
async def on_member_join(member):
  await member.send(f'**Welcome to the F Society** @{member} *Read the* <#774143716042604545> *and get your roles in* <#775269400549916702> <:ShibaHeart:793851831431200808> <@&802760617769041990> ')


client.run(os.environ['DISCORD_TOKEN'])


