import os
import discord
from discord.ext import commands
import asyncio
import random


client = commands.Bot(command_prefix =commands.when_mentioned_or('f ','F '))
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
  if arg is None:
    embed=discord.Embed(title = "The F Society", description="**HELP**", colour=0x2f3136)


    
  
  
    embed.add_field(name="• Ping",value=":placard: **f ping** Poke me... I poke you back with the BOT's Ping!",inline=True)
    embed.add_field(name="• Info",value="<a:Chat:804180442626261014> Info Commands like Avatar,Ping and much more coming soon!",inline=True)
  
    embed.add_field(name="• Utility",value="<a:MochaAngry:803227613669490719> Commands that'll be useful like snipes , editsnipes , 8ball",inline=True)
    embed.add_field(name="• Fun",value="<a:sleepingcat:799691148628852776> Fun Commands that is actually fun<:wot:790094440387182604>",inline=True)
    embed.add_field(name="• Reaction", value="<:SimpPills:774216550932545568> Non Simping Chill Reaction commands maybe ? the ones that are not cringy ofc",inline=True)
    embed.set_footer(text="Dig Bick Energy Gang | To get more information into the command do f help <command> ")
    embed.add_field(name="Making in Progress",value="*So far I only have few commands! ;-;*" , inline=False)
    embed.add_field(name="F Society",value="[Support Server](https://discord.gg/2tpP5RzWuX)" , inline=False)
    await ctx.send(embed=embed)
  elif arg in ["fun","FUN","Fun"]:
    em=discord.Embed(title="Fun Commands",color=0x2f3136)
    em.add_field(name="• Simprate",value="**f howsimp** <a:simp:775732672793411605> Gives your Simp rate!")
    em.add_field(name="• Gayrate",value="**f howgay** <a:disco_cat:799691432553873419> Gives your Gay rate!")
    em.add_field(name="• Hornyrate",value="**f howhorny** <:hmmm:790829841679253525>  Gives your Horny rate!")
    em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)
  elif arg in ['info','INFO','Info']:
    em=discord.Embed(title="Info Commands",color=0x2f3136)
    em.add_field(name="• Avatar",value="<a:Chat:804180442626261014> **f avatar** Gets the avatar of the person!",inline=True)
    em.add_field(name="• Credits",value="<a:Chat:804180442626261014> **f credits** Gets the credits of making the bot",inline=True)
    em.add_field(name="• Invite",value="<a:Chat:804180442626261014> **f invite** Gets the invite link of the bot",inline=True)
    em.add_field(name="• Links",value="<a:Chat:804180442626261014> **f links** Gets all the links related to the bot",inline=True)
    em.add_field(name="• Ping",value=":placard: **f ping** Poke me... I poke you back with the BOT's Ping!",inline=True)
    em.add_field(name="• Support",value=":placard: **f support** Bot's Support Server + Chill Server Link!",inline=True)
    em.add_field(name="• Stats",value=":placard: **f stats** Gives the stats of the bot!",inline=True)
    em.add_field(name="Coming Soon",value="In Progress")
    em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)
  elif arg in ["utility","Utility","UTILITY"]:
    embed=discord.Embed(title="Utility Commands",color=0x2f3136)
    embed.add_field(name="• BAM",value="<a:crown:793089465659949076> **f bam** Get Bammed! :P *Owner Abuse Only* <:Shiba_Cool:793772486822068224> ",inline=True)
    embed.add_field(name="• 8Ball",value=":8ball: **f eiball** Ask me a simple question predicting future I'll give my opinion!",inline=True)
    embed.add_field(name="• Snipe",value="<:Sniper:803875843507748874> **f snipe** I'll snipe the deleted message cos why not! ;)",inline=True)
    embed.add_field(name="• Edit Snipe",value="<:Target:803960603541635072> **f editsnipe** I'll snipe the edit message cos idk ask ;)",inline=True)
    embed.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  elif arg in ["reaction","Reaction","REACTION"]:
    embed=discord.Embed(title="Reaction Commands",color=0x2f3136)
    embed.add_field(name="• Bonk", value="<:wot:790094440387182604> **f bonk** Bonksss",inline=True)
    embed.add_field(name="• Punch", value="<:pepe_peeping:790829664230309888> **f punch** Punches with some beeef",inline=True)
    embed.add_field(name="• Hug", value="<:EXTRASHY:788441412872962059> **f hug** hugs platonically :D",inline=True)
    embed.add_field(name="• Kiss", value="<:oh:774246120846917633> **f kiss** kisses platonically :3",inline=True)
    embed.add_field(name="• Kill", value="<a:MochaAngry:803227613669490719> **f kill** kills with some swag",inline=True)
    embed.add_field(name="• slap", value="<:Shiba_thinking:793772530485297172> **f slaps** Slaps with some force!",inline=True)
    
    
    
    await ctx.send(embed=embed)
@client.command()
async def support(ctx):
  await ctx.send("The Bot's Support Server + Chill server  https://discord.gg/2tpP5RzWuX")
  



  




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
    em.add_field(name="Reason -",value=f":placard: You are too cool to get a BAM <:okDamn:792390256980000788> Blame <@{ctx.guild.owner_id}> For trolling you! <a:THINK_EXTREME:801464607159091201> ",inline=True)
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
      await asyncio.sleep(40)
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
      await asyncio.sleep(40)
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

hugss=['https://media.tenor.com/images/8f44c083c55620c02f59c6bea378dca4/tenor.gif','https://media.tenor.com/images/6083ba11631dd577bcc271268d010832/tenor.gif','https://media.tenor.com/images/77ea5be350828ec04edcbe4865285a77/tenor.gif','https://media.tenor.com/images/ca682cecd6bff521e400f984502f370c/tenor.gif','https://media.tenor.com/images/35fc88f417892fad929380ad78c796b9/tenor.gif','https://media.tenor.com/images/73f2117d26096fbd804c739af0c06257/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/ca1663b2092426c2d42c4c14be91cc69/tenor.gif','https://media.tenor.com/images/f1bf91d3870ed8b26367afd1b91ada9c/tenor.gif','https://media.tenor.com/images/886cb8ce1db5f0f35195c3ecf2b2fa85/tenor.gif','https://media.tenor.com/images/630087a5adbad295ea23f2042756f4df/tenor.gif']
kisses=['https://c.tenor.com/eSoJ4EYmTB8AAAAj/mochi-peach.gif','https://media.tenor.com/images/c7e53580a05faa14d94e30cfb3af5f94/tenor.gif','https://media.tenor.com/images/84fd99f1cd47a7eae6a088e5d61be0bb/tenor.gif','https://media.tenor.com/images/10f91627a6e10bcf59fae82e3a6a15a6/tenor.gif','https://media.tenor.com/images/fd65261a2c840100bd3dadd83b27f65d/tenor.gif','https://media.tenor.com/images/54f853724e8a339d894d78f8901627ba/tenor.gif','https://media.tenor.com/images/727aa9d43c7aacdaca10104cd0e6d365/tenor.gif','https://media.tenor.com/images/1827e670140cfc47c9d1571e92e2aa87/tenor.gif','https://media.tenor.com/images/68d59bb29d7d8f7895ce385869989852/tenor.gif','https://media.tenor.com/images/b020758888323338c874c549cbca5681/tenor.gif']
punchh=['https://cdn.discordapp.com/attachments/774164648093810718/806163162579730502/tenor_3.gif',"https://media.tenor.com/images/9c14d2d5dd918471954e5946166f3632/tenor.gif",'https://media.tenor.com/images/7eb5ede6402a3fb97ab9fccc81640c2c/tenor.gif','https://media.tenor.com/images/8a79543998d6878be573aab94ae86456/tenor.gif','https://media.tenor.com/images/5b668436338971d42469d7348a5340e5/tenor.gif','https://media.tenor.com/images/697ef4b275b5d9de5215a37b1e7f96da/tenor.gif','https://media.tenor.com/images/5cdcbff8c5bce802d7b65baa711f12f4/tenor.gif']
boopp=['https://media.tenor.com/images/c46116b9116e1baa24e96fa6c5a78818/tenor.gif','https://media.tenor.com/images/a02506bf918679cd3a4658dd09632341/tenor.gif','https://media.tenor.com/images/d07762ab2f5fc5d1d43525d2b3db7de8/tenor.gif','https://media.tenor.com/images/8bf3b4bec5055537dda92d86d16ea5bd/tenor.gif','https://media.tenor.com/images/2ff785b647ef22f7110b3b2599e4c847/tenor.gif','https://media.tenor.com/images/ff69974ac6a5ffa9a4ab8a59a522d04e/tenor.gif',]
slapp=['https://media.tenor.com/images/734d628ba871022bc9ae142035b969b5/tenor.gif','https://media.tenor.com/images/63c3441f0f14a753d74252a7c0247afa/tenor.gif','https://media.tenor.com/images/49b0ce2032f6134c31e1313cb078fe5a/tenor.gif','https://media.tenor.com/images/47a6be1fbc1c40c3a55c0e2c8b725603/tenor.gif','https://media.tenor.com/images/c366bb3a5d7820139646d8cdce96f7a8/tenor.gif','https://media.tenor.com/images/c5651d89a0d457a89f45b80f29ceeadb/tenor.gif','https://media.tenor.com/images/a14be99841c909a43d24b220ffebaa37/tenor.gif','https://media.tenor.com/images/a5e7b8842285b117a05a35552f586b6e/tenor.gif','https://media.tenor.com/images/53b846f3cc11c7c5fe358fc6d458901d/tenor.gif','https://media.tenor.com/images/1d8edce282f3e36abc6b730357d3cea2/tenor.gif','https://media.tenor.com/images/3f9e6d5315b421c11cff659cd4a7a25e/tenor.gif']
killl=['https://media.tenor.com/images/0df66def2ac730f8417a8dfa41dc7b91/tenor.gif','https://media.tenor.com/images/b713799e73ffe51c0268947e7708c39c/tenor.gif','https://media.tenor.com/images/f2815deb4991c4153a50801a7c95ac2c/tenor.gif','https://media.tenor.com/images/2f81a18eaa675aab3a0032df7bd65ac8/tenor.gif','https://media.tenor.com/images/6192dbf540b3a5f2e5fb8b972d2856a4/tenor.gif']
bonkk=['https://media.tenor.com/images/e1abfac2a360a1c32052135e358e092f/tenor.gif','https://media.tenor.com/images/d1108955c4fbf68fe97d41d17f3afbd2/tenor.gif','https://media.tenor.com/images/c493113cf83bb30905640b487e7ed035/tenor.gif','https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif','https://media.tenor.com/images/79c666d38d5494bad25c5c023c0bbc44/tenor.gif']
@client.command()
async def prefix(ctx):
    em=discord.Embed(description="<:bot_dev:804257409388249098> Prefix for the <@774248018802114591>  - `f ` & <@774248018802114591>",color=0x2f3136)
    em.set_author(name=ctx.guild.name,icon_url=ctx.guild.icon_url)
    em.set_footer(text="Do f help to get more info on the bot.")
    await ctx.send(embed=em)
@client.command()
async def hug(ctx ,avamember : discord.Member=None):
  if avamember is None:
    await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
  else:

    em = discord.Embed(color=0xfefec8)
    em.set_author(name=f"{ctx.author.name} hugs {avamember.name}", icon_url=ctx.author.avatar_url)
    em.set_footer(text='What a simp')
    em.set_image(url=random.choice(hugss)) 
    await ctx.send(embed=em)
@client.command()
async def kiss(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} kisses {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='What a simp smh')
      em.set_image(url=random.choice(kisses)) 
      await ctx.send(embed=em)
    
@client.command()
async def howgay(ctx, member: discord.Member=None):
  x=random.randint(1,100)
  if member is None:
    member=ctx.message.author.name
    em = discord.Embed(title="Gay Rate",description=f'<a:disco_cat:799691432553873419> You are {x} % Gay',color=0x2f3136)
  
   
    
    await ctx.send(embed=em)
  else:

    em = discord.Embed(title="Gay Rate",description=f'<a:disco_cat:799691432553873419> {member.name} is {x} % Gay',color=0x2f3136)
  
   
    
    await ctx.send(embed=em) 
@client.command()
async def howhorny(ctx, member: discord.Member=None):
  x=random.randint(1,100)
  if member is None:
    member=ctx.message.author.name
    em = discord.Embed(title="Horny JAIL Says...",description=f'<:hmmm:790829841679253525> You are {x} % Horny',color=0x2f3136)
  
   
    
    await ctx.send(embed=em)
  else:

    em = discord.Embed(title="Horny JAIL Says...",description=f'<:hmmm:790829841679253525> {member.name} is {x} % Horny',color=0x2f3136)
  
   
    
    await ctx.send(embed=em)
@client.command()
async def howsimp(ctx, member: discord.Member=None):
  x=random.randint(1,100)
  if member is None:
    member=ctx.message.author.name
    em = discord.Embed(title="Simp Rate",description=f'<a:simp:775732672793411605> You are {x} % Simp',color=0x2f3136)
  
   
    
    await ctx.send(embed=em)
  else:

    em = discord.Embed(title="Simp Rate",description=f'<a:simp:775732672793411605> {member.name} is {x} % Simp',color=0x2f3136)
  
   
    
    await ctx.send(embed=em) 

@client.command()
async def kill(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} kills {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='I-')
      em.set_image(url=random.choice(killl)) 
      await ctx.send(embed=em)
  
@client.command()
async def slap(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} slaps {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='Good slap ngl')
      em.set_image(url=random.choice(slapp)) 
      await ctx.send(embed=em)
@client.command()
async def bonk(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} bonks {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text=';-;')
      em.set_image(url=random.choice(bonkk)) 
      await ctx.send(embed=em)
@client.command()
async def punch(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} punches {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='We got some beef here!')
      em.set_image(url=random.choice(punchh)) 
      await ctx.send(embed=em)
@client.command()
async def invite(ctx):
  x="https://discord.com/oauth2/authorize?client_id=774248018802114591&scope=bot&permissions=1614146624"
  embed=discord.Embed(title = "The F Society", description="<:AlienSign:797352295779270666> [Invite Link]({})".format(x), colour=0x2f3136)
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  await ctx.send(embed=embed)
@client.command()
async def links(ctx):
  x="https://discord.com/oauth2/authorize?client_id=774248018802114591&scope=bot&permissions=1614146624"
  embed=discord.Embed(title = "The F Society", colour=0x2f3136)
  embed.add_field(name="Bot Invite Link",value="<a:Chat:804180442626261014> [Invite Link]({})".format(x),inline=False)
  embed.add_field(name="F Society Link",value="<a:Chat:804180442626261014> [Support Server](https://discord.gg/2tpP5RzWuX)",inline=False)
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  await ctx.send(embed=embed)
@client.command()
async def credits(ctx):
  e=discord.Embed(title="The F Society",color=0x2f3136)
  e.add_field(name="<:bot_dev:804257409388249098> BOT DEV",value="Creator - **KaZE#5043**",inline=False)
  e.add_field(name=":art: Avatar ",value="Artist - **RMV**",inline=False)
  e.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  e.set_footer(text="F SOCIETY")
  await ctx.send(embed=e)
  
@client.command()
async def stats(ctx):
  dpyversion=discord.__version__
  servercount=len(client.guilds)
  membercount=len(set(client.get_all_members()))
  x=f'''<:BugHunter:803977931528994836> Ping - {round(client.latency *1000)}ms
  <a:Chat:804180442626261014>Server Count - {servercount} Servers
  <:AlienSign:797352295779270666> Member Count- {membercount} Members
  :placard: Discord Version - {dpyversion}'
  <:DarkHypesquad:803977958108692570> Language - Python [discord.py]'''
  embed=discord.Embed(title="The F Society",description=f"BOT STATS /n {x}",colour=0x2f3136)
  
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  await ctx.send(embed=embed)






client.run(os.environ['DISCORD_TOKEN'])


