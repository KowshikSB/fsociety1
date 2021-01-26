import os
import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = '^')
client.remove_command("help")


ba=["Ask Me If I Care","Dumb Question Ask Another", "Forget About It" , "In Your Dreams" , "Not A Chance" , "Obviously" , "What Do You Think?" ,  "Who Cares?" , "You've Got To Be Kidding","Yeah Right"," You Wish","Absolutely", "Unclear Ask Later","Chances Aren't Good", "Ask KaZE He's Wisest Man here", "Indications Say Yes" , "No Doubt About It","The Stars Say No","You Can Count On It"]
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
async def eiball(ctx, arg=None):
  ctx = await ctx.channel.send('<:blobhyperthink:774246322194612224>')
  await asyncio.sleep(1)
    
  content=discord.Embed(color=0x2f3136 , description =":8ball: {}".format(random.choice(ba)))
  await ctx.channel.edit(Embed=content)


  
    
  embed.set_footer(text="Dig Bick Energy Gang")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/774143806601822208/778997559313301504/ezgif.com-gif-maker_2.gif')
  embed.add_field(name="• Ping",value=":placard: Poke me... I poke you back with the BOT's Ping!",inline=False)
  embed.add_field(name="• BAM",value="<a:crown:793089465659949076> Get Bammed <:Shiba_Cool:793772486822068224> ||OWNER Only Command|| ",inline=False)
  embed.add_field(name="Making in Progress",value="*So far I only have few commands! ;-; Blame it on* <@261742964441612298>" , inline=False)
  await ctx.send(embed=embed)

em=discord.Embed(title = "The F Society", description= "**You have Been Bammed In F Society!**", colour=0x2f3136)
em.set_footer(text="Dig Bick Energy Gang")
em.set_thumbnail(url='https://cdn.discordapp.com/attachments/774143806601822208/778997559313301504/ezgif.com-gif-maker_2.gif')
em.add_field(name="Reason -",value=":placard: You are too cool to get a BAM <:okDamn:792390256980000788> Blame <@261742964441612298> For trolling you! <a:THINK_EXTREME:801464607159091201> ",inline=True)
@client.command()
@commands.has_role('+')  
async def bam(ctx,user_id=None,args=em):
 
  if user_id!=None and args !=None:
    try:
      target = await client.fetch_user(user_id)
      await target.send(embed=args)
      
      await ctx.send("The User is Bammed <:okDamn:792390256980000788> ")
    except:
      await ctx.channel.send("`Couldn't DM the given user`") 



  

client.run(os.environ['DISCORD_TOKEN'])


