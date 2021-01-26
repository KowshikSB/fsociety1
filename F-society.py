

import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '^')
client.remove_command("help")



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The Ded Chat ;-;"))
#Runs when bot is online and active  
  print("BOT IS READY")
@client.command()
async def ping(ctx, arg=None):
  if arg=="Pong":
    await ctx.send("Sexy job you just ponged yourself <a:shiba_Sexy_wink:794199806833590302> ")
  else:
    await ctx.send(f'<:wot:790094440387182604> Pong! `{round(client.latency *1000)}ms`')
@client.group(invoke_whithout_command=True)
async def help(ctx):
  em = discord.Embed(title = "The F Society" , descritption = "**Help Commands**",color=#2f3136)
  em.add_field(name="Ping",value="^ping - *So far we got Ping command ;-;* <@261742964441612298> *is Making me more useful* <:angry_flushed:803240935433437194>")
    
  await ctx.(Embed=em)
 

client.run(os.environ['DISCORD_TOKEN'])


