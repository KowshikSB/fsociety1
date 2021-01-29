import os
import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix =commands.when_mentioned_or('f '))
client.remove_command("help")


ba=["Ask Me If I Care","Dumb Question Ask Another", "Forget About It" , "In Your Dreams" , "Not A Chance" , "ofc"," yeasss","I'd say yes but you have to get me some crack B)","You may rely on it","Obviously" , "What Do You Think?" ,  "Who Cares?" , "You've Got To Be Kidding","Yeah Right"," You Wish","Absolutely", "Unclear Ask Later","Chances Aren't Good", "Ask <@261742964441612298> He's the Wisest Man here", "Indications Say Yes" , "No Doubt About It","The Stars Say No","You Can Count On It"]
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
    await ctx.send(f'<:BugHunter:803977931528994836> Pong! `{round(client.latency *1000)}ms`')
@client.command()
async def help(ctx, arg=None):
  embed=discord.Embed(title = "The F Society", description= "**HELP**", colour=0x2f3136)


    
  embed.set_footer(text="Dig Bick Energy Gang")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/774143806601822208/778997559313301504/ezgif.com-gif-maker_2.gif')
  embed.add_field(name="• Ping",value=":placard: **f ping** Poke me... I poke you back with the BOT's Ping!",inline=True)
  embed.add_field(name="• BAM",value="<a:crown:793089465659949076> **f bam** Get Bammed! :P *Owner Abuse Only* <:Shiba_Cool:793772486822068224> ",inline=True)
  embed.add_field(name="• 8Ball",value=":8ball: **f eiball** Ask me a simple question predicting future I'll give my opinion!",inline=True)
  embed.add_field(name="• Snipe",value="<:Sniper:803875843507748874> **f snipe** I'll snipe the deleted message cos why not! ;)",inline=True)
  embed.add_field(name="• Edit Snipe",value="<:Target:803960603541635072> **f editsnipe** I'll snipe the edit message cos idk ask ;)",inline=True)
  embed.add_field(name="• Avatar",value="<a:Chat:804180442626261014> **f avatar** Gets the avatar of the person!",inline=True)
  embed.add_field(name="Making in Progress",value="*So far I only have few commands! ;-;" , inline=False)
  await ctx.send(embed=embed)

em=discord.Embed(title = "The F Society", description= "**You have Been Bammed In F Society!**", colour=0x2f3136)
em.set_footer(text="Dig Bick Energy Gang")
icon=Guild.icon_url
em.set_thumbnail(url=icon)
em.add_field(name="Reason -",value=":placard: You are too cool to get a BAM <:okDamn:792390256980000788> Blame <@261742964441612298> For trolling you! <a:THINK_EXTREME:801464607159091201> ",inline=True)
@client.command()
async def eiball(ctx, arg=None):
 
    
  content=discord.Embed(color=0x2f3136 , description ="<:blobhyperthink:774246322194612224>:8ball: {}".format(random.choice(ba)))
  msg = await ctx.send(embed=content)
  await msg.add_reaction("<:wot:790094440387182604>") #\U0001f3b1
  
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

client.sniped_messages = {}
@client.event
async def on_message_delete(message):
    if message.author != client.user: 
      client.sniped_messages[message.channel.id]=(message.content,message.author,message.channel.name,message.created_at)
      await asyncio.sleep(20)
      client.sniped_messages[message.channel.id]=None

@client.command()
async def snipe(ctx):
    try:
      contents,author,channel_name,time=client.sniped_messages[ctx.channel.id]
      embed=discord.Embed(description=contents,color=0x2f3136,timestamp=time)
      embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
      embed.set_footer(text=f'Deleted in: #{channel_name}')
      await ctx.channel.send(embed=embed,delete_after=60)
    except:
      await ctx.channel.send("<a:potato_rage:788063034701906001> *Dont waste my ammo `;-;` Nothing to snipe!*")
client.esniped_messages={}
@client.event
async def on_message_edit(before,after):
    if after.author != client.user: 
      client.esniped_messages[before.channel.id]=(before.content,before.author,before.channel.name,before.created_at)
      await asyncio.sleep(20)
      client.esniped_messages[before.channel.id]=None

@client.command()
async def editsnipe(ctx):
    try:
      contents,author,channel_name,time=client.esniped_messages[ctx.channel.id]
      embed=discord.Embed(description=contents,color=0x2f3136,timestamp=time)
      embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
      embed.set_footer(text=f'Edited: #{channel_name}')
      await ctx.channel.send(embed=embed,delete_after=60)
    except:
      await ctx.channel.send("<a:potato_rage:788063034701906001> *Dont waste my ammo `;-;` Nothing to snipe!*",delete_after=10)
@client.command()
async def avatar(ctx ,avamember : discord.Member=None):
  if avamember is None:
    avamember=ctx.message.author 
    
  userAvatarUrl = avamember.avatar_url
  em = discord.Embed(title=f"Avatar of {avamember}", color=0x2f3136)
  em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)
  em.set_image(url=userAvatarUrl) 
    
  await ctx.send(embed=em) 
@client.command()
async def prefix(ctx):
    em=discord.Embed(description="<:bot_dev:804257409388249098> Prefix for this Guild - `f ` & <@774248018802114591>",color=0x2f3136)
    em.set_author(name='The F Society',icon_url="https://cdn.discordapp.com/attachments/774143806601822208/778997559313301504/ezgif.com-gif-maker_2.gif")
    em.set_footer(text="Do f help to get more info on the bot.")
    await ctx.send(embed=em)
  

client.run(os.environ['DISCORD_TOKEN'])


