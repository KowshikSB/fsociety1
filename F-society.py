import os
import discord
from discord.ext import commands
import asyncio
import random


client = commands.Bot(command_prefix =commands.when_mentioned_or('f '))
client.remove_command("help")
command_prefix =commands.when_mentioned_or('f ')


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
  embed=discord.Embed(title = "The F Society", description="**HELP**", colour=0x2f3136)


    
  embed.set_footer(text="Dig Bick Energy Gang")
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name="• Ping",value=":placard: **f ping** Poke me... I poke you back with the BOT's Ping!",inline=True)
  embed.add_field(name="• BAM",value="<a:crown:793089465659949076> **f bam** Get Bammed! :P *Owner Abuse Only* <:Shiba_Cool:793772486822068224> ",inline=True)
  embed.add_field(name="• 8Ball",value=":8ball: **f eiball** Ask me a simple question predicting future I'll give my opinion!",inline=True)
  embed.add_field(name="• Snipe",value="<:Sniper:803875843507748874> **f snipe** I'll snipe the deleted message cos why not! ;)",inline=True)
  embed.add_field(name="• Edit Snipe",value="<:Target:803960603541635072> **f editsnipe** I'll snipe the edit message cos idk ask ;)",inline=True)
  embed.add_field(name="• Avatar",value="<a:Chat:804180442626261014> **f avatar** Gets the avatar of the person!",inline=True)
  embed.add_field(name="• Hug", value="<:EXTRASHY:788441412872962059> hugs platonically :D",inline=True)
  embed.add_field(name="• Kiss", value="<:oh:774246120846917633> kisses platonically :3",inline=True)
  embed.add_field(name="Making in Progress",value="*So far I only have few commands! ;-;*" , inline=False)
  await ctx.send(embed=embed)


@client.command()
async def eiball(ctx, arg=None):
 
    
  content=discord.Embed(color=0x2f3136 , description ="<:blobhyperthink:774246322194612224>:8ball: {}".format(random.choice(ba)))
  msg = await ctx.send(embed=content)
  await msg.add_reaction("<:wot:790094440387182604>") #\U0001f3b1
  
@client.command()

async def bam(ctx,user_id=None,args=None):
  if ctx.author.id==ctx.guild.owner_id:
    em=discord.Embed(title = ctx.guild.name, description= "**You have Been Bammed In {}!**".format(ctx.guild.name), colour=0x2f3136)
    em.set_footer(text="Dig Bick Energy Gang")
    icon=ctx.guild.icon_url
    em.set_thumbnail(url=icon)
    em.add_field(name="Reason -",value=":placard: You are too cool to get a BAM <:okDamn:792390256980000788> Blame <@261742964441612298> For trolling you! <a:THINK_EXTREME:801464607159091201> ",inline=True)
    args=em
    if user_id!=None and args !=None:
      try:
        target = await client.fetch_user(user_id)
        await target.send(embed=args)
      
        await ctx.send("The User is Bammed <:okDamn:792390256980000788> ")
      except:
        await ctx.channel.send("`Couldn't DM the given user`") 
  else:
    await ctx.send("You can't Bam noob!")

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
    em.set_author(name=ctx.guild.name,icon_url=ctx.guild.icon_url)
    em.set_footer(text="Do f help to get more info on the bot.")
    await ctx.send(embed=em)
hugss=['https://media.tenor.com/images/8f44c083c55620c02f59c6bea378dca4/tenor.gif','https://media.tenor.com/images/6083ba11631dd577bcc271268d010832/tenor.gif','https://media.tenor.com/images/77ea5be350828ec04edcbe4865285a77/tenor.gif'
'https://media.tenor.com/images/ca682cecd6bff521e400f984502f370c/tenor.gif','https://media.tenor.com/images/35fc88f417892fad929380ad78c796b9/tenor.gif''https://media.tenor.com/images/73f2117d26096fbd804c739af0c06257/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/ca1663b2092426c2d42c4c14be91cc69/tenor.gif','https://media.tenor.com/images/f1bf91d3870ed8b26367afd1b91ada9c/tenor.gif','https://media.tenor.com/images/886cb8ce1db5f0f35195c3ecf2b2fa85/tenor.gif','https://media.tenor.com/images/630087a5adbad295ea23f2042756f4df/tenor.gif']
kissss=['https://c.tenor.com/eSoJ4EYmTB8AAAAj/mochi-peach.gif','https://media.tenor.com/images/84fd99f1cd47a7eae6a088e5d61be0bb/tenor.gif','https://media.tenor.com/images/10f91627a6e10bcf59fae82e3a6a15a6/tenor.gif','https://media.tenor.com/images/fd65261a2c840100bd3dadd83b27f65d/tenor.gif','https://media.tenor.com/images/54f853724e8a339d894d78f8901627ba/tenor.gif','https://media.tenor.com/images/727aa9d43c7aacdaca10104cd0e6d365/tenor.gif','https://media.tenor.com/images/1827e670140cfc47c9d1571e92e2aa87/tenor.gif,https://media.tenor.com/images/68d59bb29d7d8f7895ce385869989852/tenor.gif','https://media.tenor.com/images/b020758888323338c874c549cbca5681/tenor.gif']
@client.command()
async def hug(ctx ,avamember : discord.Member=None):
  if avamember is None:
    await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
  else:

    em = discord.Embed(color=0xfefec8)
    em.set_author(name=f"{ctx.author.name} hugs {avamember.name}", url=ctx.author.avatar_url)
    em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    em.set_image(url=random.choice(hugss)) 
    await ctx.send(embed=em)
@client.command()
async def kiss(ctx ,avamember : discord.Member=None):
  if avamember is None:
    await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
  else:

    em = discord.Embed(color=0xfefec8)
    em.set_author(name=f"{ctx.author.name} kisses {avamember.name}", url=ctx.author.avatar_url)
    em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    em.set_image(url=random.choice(kissss)) 
    await ctx.send(embed=em)
    

client.run(os.environ['DISCORD_TOKEN'])


