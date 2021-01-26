

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
@client.command()
async def help(ctx, arg=None):
  embed=discord.Embed(title = "The F Society", description= "**HELP**", colour=0x2f3136)
  
  embed.set_footer(text="Dig Bick Energy Gang")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/774143806601822208/778997559313301504/ezgif.com-gif-maker_2.gif')
  embed.add_field(name="Ping",value=":placard: So far I only have the Ping Command ;-; Blame it on <@261742964441612298>",inline=False)
  await ctx.send(embed=embed)
client.run(os.environ['DISCORD_TOKEN'])


