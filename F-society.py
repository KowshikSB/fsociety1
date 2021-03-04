import os

import discord
from discord import message
from discord import channel
from discord.colour import Color
from discord.enums import ContentFilter, Status
from discord.ext import commands
import asyncio
import random
import platform
from discord import Intents
from discord.ext import tasks
from discord.utils import get 




client = commands.Bot(command_prefix =commands.when_mentioned_or('f ','F '),intents=discord.Intents.all())
client.remove_command("help")

command_prefix =commands.when_mentioned_or('f ')




async def status():
  while True:
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing , name="With your mama"))
    await asyncio.sleep(900)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="Kaze"))
    await asyncio.sleep(900)
   
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching, name="the rule breakers"))
    await asyncio.sleep(900)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="F Society"))
    await asyncio.sleep(900)
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The Ded Chat ;-;"))
    await asyncio.sleep(900)
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="You"))
    await asyncio.sleep(900)
    
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="SIMPS"))
    await asyncio.sleep(900)

@client.event
async def on_ready():
  #client.load_extension("onMessage")
  print("BOT IS READY")
  

#FE6450-Red
#4C73FE-Blue
#FEE064-Yellow

  client.loop.create_task(status())




@client.command()
async def ping(ctx, arg=None):
  if arg=="Pong":
    await ctx.send("Sexy job you just ponged yourself <a:shiba_Sexy_wink:794199806833590302> ")
  else:
    await ctx.send(f'<:BugHunter:803977931528994836> Pong! `{round(client.latency *1000)}ms`')
@client.command()
async def help(ctx, arg=None):
  if arg is None:
    embed=discord.Embed(title = "The F Society", description="**HELP**",color=0x2f3136)


    
  
  
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name=":placard: Info",value="• **ping** • **avatar** • **membercount**  • **stats**",inline=False)
  
    embed.add_field(name=":placard: Utility",value="• **snipe** • **clear** • **editsnipe** • **confess** • **suggest** • **userinfo**",inline=False)
    embed.add_field(name=":placard: Fun",value="• **howsimp** • **howgay** • **howorny** • **pp** • **8ball** • **bam** ",inline=False)
    embed.add_field(name=":placard: Reaction", value="• **kill** • **slap** • **kiss** • **boop** • **hug** • **bonk** • **pat** • **punch**",inline=False)
    embed.set_footer(text="Dig Bick Energy Gang")
    embed.add_field(name="Making in Progress",value="*So far I only have few commands! ;-;*" , inline=False)
    embed.add_field(name="The F Society",value="Prefixes `f ` ,`F `, <@774248018802114591>" , inline=False)
    await ctx.send(embed=embed)
 

@client.event
async def on_member_join(member):

  
  if member.guild.id==725302478823751702:
    x='''<a:crown:793089465659949076> *Head over to <#774143716042604545> for Basic Server Rules to Chill*
<a:crown:793089465659949076>  *Get roles in* <#775269400549916702>
<a:crown:793089465659949076> *Tell us little about yourself!* <#810394496264699924>
<a:crown:793089465659949076> Talk in <#774155081922773022>  ;-;'''
    
    em=discord.Embed(title="WELCOME TO F Society!",description=x,color=0x2f3136)
    em.set_author(name=f'{member.name}#{member.discriminator}',icon_url=member.avatar_url)
    em.set_thumbnail(url=member.guild.icon_url)
    em.set_footer(text="K E E P C H I L L I N G")
    guild=client.get_guild(725302478823751702)
    channel=guild.get_channel(774155081922773022)
    await channel.send(f'<:Shiba_thinking:793772530485297172> {member.mention} <@&802760617769041990>',embed=em)
    




  




@client.command(name='eiball',aliases=['8ball','8b'])
async def eiball(ctx, arg=None):
  ba=["Ask Me If I Care","Dumb Question Ask Another", "Forget About It" , "In Your Dreams" , "Not A Chance" , "ofc"," yeasss","I'd say yes but you have to get me some crack B)","You may rely on it","Obviously" , "What Do You Think?" ,  "Who Cares?" , "You've Got To Be Kidding","Yeah Right"," You Wish","Absolutely", "Unclear Ask Later","Chances Aren't Good", f"Ask <@{ctx.guild.owner_id}> the Wisest Person here", "Indications Say Yes" , "No Doubt About It","The Stars Say No","You Can Count On It"]
    
  content=discord.Embed(color=0x2f3136 , description ="<:blobhyperthink:774246322194612224>:8ball: {}".format(random.choice(ba)))
  msg = await ctx.send(embed=content)
  await msg.add_reaction("<:wot:790094440387182604>") #\U0001f3b1
  
@client.command()
async def bam(ctx,user_id=None,args=None):
  if ctx.author.id==ctx.guild.owner_id:
    uid=int(user_id)
    em=discord.Embed(title = ctx.guild.name, description= "**You have Been Bammed In {}!**".format(ctx.guild.name), colour=0x2f3136)
    em.set_footer(text="Dig Bick Energy Gang")
    icon=ctx.guild.icon_url
    em.set_thumbnail(url=icon)
    em.add_field(name="Reason -",value=f":placard: You are too cool to get a BAM <:okDamn:792390256980000788> Blame <@{ctx.guild.owner_id}> For trolling you! <a:THINK_EXTREME:801464607159091201> ",inline=True)
    args=em
    guild=ctx.guild
    if guild.get_member(uid)!=None:
    
      if user_id!=None and args !=None:
        
        try:
          target = await client.fetch_user(user_id)
          await target.send(embed=args)
        
          await ctx.send("The User is Bammed <:okDamn:792390256980000788> ")
        except:
          await ctx.channel.send("`Couldn't DM the given user`") 
    else:
      await ctx.send("The user is not in the guild!")
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
      await ctx.channel.send("<a:potato_rage:788063034701906001> *Who pays for the ammo? `;-;` Nothing to snipe!*")
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
      await ctx.channel.send("<a:potato_rage:788063034701906001> *Who pays for the ammo? `;-;` Nothing to snipe!*",delete_after=10)
@client.command(name='avatar',aliases=["av"])
async def avatar(ctx ,avamember : discord.Member=None):
  if avamember is None:
    avamember=ctx.message.author 
    
  userAvatarUrl = avamember.avatar_url
  em = discord.Embed(title=f"Avatar of {avamember}", color=0x2f3136)
  em.set_footer(text=f'Requested by {ctx.author.name}',icon_url=ctx.author.avatar_url)
  em.set_image(url=userAvatarUrl) 
    
  await ctx.send(embed=em) 

hugss=['https://media.tenor.com/images/8f44c083c55620c02f59c6bea378dca4/tenor.gif','https://media.tenor.com/images/6083ba11631dd577bcc271268d010832/tenor.gif','https://media.tenor.com/images/77ea5be350828ec04edcbe4865285a77/tenor.gif','https://media.tenor.com/images/ca682cecd6bff521e400f984502f370c/tenor.gif','https://media.tenor.com/images/35fc88f417892fad929380ad78c796b9/tenor.gif','https://media.tenor.com/images/73f2117d26096fbd804c739af0c06257/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif','https://media.tenor.com/images/ca1663b2092426c2d42c4c14be91cc69/tenor.gif','https://media.tenor.com/images/f1bf91d3870ed8b26367afd1b91ada9c/tenor.gif','https://media.tenor.com/images/886cb8ce1db5f0f35195c3ecf2b2fa85/tenor.gif','https://media.tenor.com/images/630087a5adbad295ea23f2042756f4df/tenor.gif']
kisses=['https://c.tenor.com/eSoJ4EYmTB8AAAAj/mochi-peach.gif','https://media.tenor.com/images/d1108955c4fbf68fe97d41d17f3afbd2/tenor.gif','https://media.tenor.com/images/6e4be7dcabb41ee76f2372f0492fc107/tenor.gif','https://media.tenor.com/images/c7e53580a05faa14d94e30cfb3af5f94/tenor.gif','https://media.tenor.com/images/84fd99f1cd47a7eae6a088e5d61be0bb/tenor.gif','https://media.tenor.com/images/10f91627a6e10bcf59fae82e3a6a15a6/tenor.gif','https://media.tenor.com/images/fd65261a2c840100bd3dadd83b27f65d/tenor.gif','https://media.tenor.com/images/54f853724e8a339d894d78f8901627ba/tenor.gif','https://media.tenor.com/images/727aa9d43c7aacdaca10104cd0e6d365/tenor.gif','https://media.tenor.com/images/1827e670140cfc47c9d1571e92e2aa87/tenor.gif','https://media.tenor.com/images/68d59bb29d7d8f7895ce385869989852/tenor.gif','https://media.tenor.com/images/b020758888323338c874c549cbca5681/tenor.gif']
punchh=['https://cdn.discordapp.com/attachments/774164648093810718/806163162579730502/tenor_3.gif',"https://media.tenor.com/images/9c14d2d5dd918471954e5946166f3632/tenor.gif",'https://media.tenor.com/images/7eb5ede6402a3fb97ab9fccc81640c2c/tenor.gif','https://media.tenor.com/images/8a79543998d6878be573aab94ae86456/tenor.gif','https://media.tenor.com/images/5b668436338971d42469d7348a5340e5/tenor.gif','https://media.tenor.com/images/697ef4b275b5d9de5215a37b1e7f96da/tenor.gif','https://media.tenor.com/images/5cdcbff8c5bce802d7b65baa711f12f4/tenor.gif']
boopp=['https://media.tenor.com/images/c46116b9116e1baa24e96fa6c5a78818/tenor.gif','https://media.tenor.com/images/a02506bf918679cd3a4658dd09632341/tenor.gif','https://media.tenor.com/images/d07762ab2f5fc5d1d43525d2b3db7de8/tenor.gif','https://media.tenor.com/images/8bf3b4bec5055537dda92d86d16ea5bd/tenor.gif','https://media.tenor.com/images/2ff785b647ef22f7110b3b2599e4c847/tenor.gif','https://media.tenor.com/images/ff69974ac6a5ffa9a4ab8a59a522d04e/tenor.gif',]
slapp=['https://media.tenor.com/images/734d628ba871022bc9ae142035b969b5/tenor.gif','https://media.tenor.com/images/63c3441f0f14a753d74252a7c0247afa/tenor.gif','https://media.tenor.com/images/49b0ce2032f6134c31e1313cb078fe5a/tenor.gif','https://media.tenor.com/images/47a6be1fbc1c40c3a55c0e2c8b725603/tenor.gif','https://media.tenor.com/images/c366bb3a5d7820139646d8cdce96f7a8/tenor.gif','https://media.tenor.com/images/c5651d89a0d457a89f45b80f29ceeadb/tenor.gif','https://media.tenor.com/images/a14be99841c909a43d24b220ffebaa37/tenor.gif','https://media.tenor.com/images/a5e7b8842285b117a05a35552f586b6e/tenor.gif','https://media.tenor.com/images/53b846f3cc11c7c5fe358fc6d458901d/tenor.gif','https://media.tenor.com/images/1d8edce282f3e36abc6b730357d3cea2/tenor.gif','https://media.tenor.com/images/3f9e6d5315b421c11cff659cd4a7a25e/tenor.gif']
killl=['https://media.tenor.com/images/0df66def2ac730f8417a8dfa41dc7b91/tenor.gif','https://media.tenor.com/images/4b210bcaafec30d386d43f0ae577fb93/tenor.gif','https://media.tenor.com/images/b713799e73ffe51c0268947e7708c39c/tenor.gif','https://media.tenor.com/images/f2815deb4991c4153a50801a7c95ac2c/tenor.gif','https://media.tenor.com/images/2f81a18eaa675aab3a0032df7bd65ac8/tenor.gif','https://media.tenor.com/images/6192dbf540b3a5f2e5fb8b972d2856a4/tenor.gif']
bonkk=['https://media.tenor.com/images/e1abfac2a360a1c32052135e358e092f/tenor.gif','https://media.tenor.com/images/c493113cf83bb30905640b487e7ed035/tenor.gif','https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif','https://media.tenor.com/images/79c666d38d5494bad25c5c023c0bbc44/tenor.gif']
patt=['https://media.tenor.com/images/69fb17b3eafe27df334f9f873473d531/tenor.gif','https://media.tenor.com/images/21c1228517cafcd13dff38e2253b4713/tenor.gif','https://media.tenor.com/images/19c555af496d14808aa5d9bd8277c937/tenor.gif','https://media.tenor.com/images/fa9ad7f4ecfad744aec37241cce2cecc/tenor.gif','https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif','https://media.tenor.com/images/dc61bf036b96b9a321943493c55ad8a4/tenor.gif']

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

    em = discord.Embed(color=0xFEE064)
    em.set_author(name=f"{ctx.author.name} hugs {avamember.name}", icon_url=ctx.author.avatar_url)
    em.set_footer(text='What a simp')
    em.set_image(url=random.choice(hugss)) 
    await ctx.send(embed=em)
@client.command()
async def boop(ctx ,avamember : discord.Member=None):
  if avamember is None:
    await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
  else:

    em = discord.Embed(color=0xFEE064)
    em.set_author(name=f"{ctx.author.name} boops {avamember.name}", icon_url=ctx.author.avatar_url)
    em.set_footer(text='huh')
    em.set_image(url=random.choice(boopp)) 
    await ctx.send(embed=em)
@client.command()
async def kiss(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xFEE064)
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
async def pp(ctx, member: discord.Member=None):
  x=random.randint(1,20)
  y="8"
  d="D"
  c=y+"="*x+d
  if member is None:
    member=ctx.message.author.name
    if x <=10:
      z=(f''' Your PP Size..
      is **{c}** ''')
      em=discord.Embed(title="<:pepe_peeping:790829664230309888> Peepee Sizer",description=f'{z}',color=0x2f3136)
      await ctx.send("<:smolpp:781375654527893560>",embed=em)
      
    else:
      z=(f''' Your PP Size..
      **{c}**  ''')
      em=discord.Embed(title="<:pepe_peeping:790829664230309888> Peepee Sizer",description=f'{z}',color=0x2f3136)
      await ctx.send("<:BigPP:781375681463713842>",embed=em)
      
      
  else:
    if x<=10:
      z=(f''' {member.name}'s PP Size..
      **{c}** ''')
      em=discord.Embed(title="<:pepe_peeping:790829664230309888> Peepee Sizer",description=f'{z}',color=0x2f3136)
      await ctx.send("<:smolpp:781375654527893560>",embed=em)
      

    else:
      
      z=(f'''{member.name}'s Your PP Size..
      **{c}** ''')
      em=discord.Embed(title="<:pepe_peeping:790829664230309888> Peepee Sizer",description=f'{z}',color=0x2f3136)
      await ctx.send("<:BigPP:781375681463713842>",embed=em)
      


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
async def pat(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xfefec8)
      em.set_author(name=f"{ctx.author.name} pats {avamember.name}", icon_url=ctx.author.avatar_url)
      
      em.set_image(url=random.choice(patt)) 
      await ctx.send(embed=em)
  
@client.command()
async def slap(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xFEE064)
      em.set_author(name=f"{ctx.author.name} slaps {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='Good slap ngl')
      em.set_image(url=random.choice(slapp)) 
      await ctx.send(embed=em)
@client.command()
async def bonk(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xFEE064)
      em.set_author(name=f"{ctx.author.name} bonks {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text=';-;')
      em.set_image(url=random.choice(bonkk)) 
      await ctx.send(embed=em)
@client.command()
async def punch(ctx ,avamember : discord.Member=None):
    if avamember is None:
      await ctx.send("<a:rage_smash:799276770091859968> *You need to mention a person*")
    
    else:

      em = discord.Embed(color=0xFEE064)
      em.set_author(name=f"{ctx.author.name} punches {avamember.name}", icon_url=ctx.author.avatar_url)
      em.set_footer(text='We got some beef here!')
      em.set_image(url=random.choice(punchh)) 
      await ctx.send(embed=em)
@client.command()
async def invite(ctx):
  await ctx.send('<a:Chat:790568691888029726> *F Society Invite link* - https://discord.gg/2tpP5RzWuX')

@client.command()
async def credits(ctx):
  e=discord.Embed(title="The F Society",color=0x2f3136)


  e.add_field(name="<:bot_dev:804257409388249098> Dev",value='Kaze#0002',inline=False)
  
  e.add_field(name="Artist",value="[Nexin](https://twitter.com/nexinwah)",inline=False)
  
  e.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  e.set_footer(text="F SOCIETY")
  await ctx.send(embed=e)
  
@client.command()
async def stats(ctx):
  
  dpyversion=discord.__version__
  servercount=len(client.guilds)
  pythonversion=platform.python_revision()
  client.fetch_guilds
  membercount=len(set(client.get_all_members()))
  x=f'''**BOT STATS**
  <:BugHunter:803977931528994836> Ping - {round(client.latency *1000)}ms

  <a:Chat:804180442626261014>Server Count - {servercount} Servers
  
  <:AlienSign:797352295779270666> Member Count - {membercount} Members

  :placard: Discord.py - {dpyversion}

  <:DarkHypesquad:803977958108692570> Language - Python {pythonversion}'''
  embed=discord.Embed(title="The F Society",description=x,colour=0x2f3136)
  
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024")
  await ctx.send(embed=embed)
@client.command()
async def membercount(ctx):
  x=ctx.guild.member_count
  em=discord.Embed(title=ctx.guild.name,description=f"**Member Count** - {x}",color=0x2f3136)
  em.set_thumbnail(url=ctx.guild.icon_url)
  em.set_footer(text="Dig Bick Energy")
  await ctx.send(embed=em)





@client.command()
async def suggest(ctx,s):
  
  if ctx.guild.id==725302478823751702:
    if s!=None:
      
      
      await ctx.message.add_reaction("<a:tickup:774207637184839680>")
      guild=client.get_guild(725302478823751702)
      channel=guild.get_channel(778960593393549333)
      suggestion=ctx.message.content[9::]

      suggestEmbed = discord.Embed(colour =0x2f3136)
      suggestEmbed.set_thumbnail(url=ctx.guild.icon_url)
      suggestEmbed.set_author(name=f'Suggested by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
    
      suggestEmbed.set_footer(text=f'ID - {ctx.message.author.id}')
      suggestEmbed.add_field(name = 'SUGGESTION', value = f'• {suggestion}')

      x=await channel.send(embed=suggestEmbed)
      await x.add_reaction("<a:yes:774149959846068244>")
      await x.add_reaction("<:neutral:812556400265527296>")
      await x.add_reaction("<a:no:774149903878062091>")
    else:
      await ctx.iend("Give a suggestion to suggest")


Mutes=[]
@client.command()
@commands.has_role('STAFF TEAM')  
async def cmute(ctx,id,*,reason=None):
  if reason is not None: 
    global Mutes
    if int(id) not in Mutes:
      guild=client.get_guild(725302478823751702)
      log=guild.get_channel(802510538021011466)
      i=int(id)
      if i!=261742964441612298:
        Mutes.append(i)
        print(Mutes)
        await ctx.send("The User is now blacklisted")
        await log.send(f'<@{id}> is now blacklisted from confessions. Reason = {reason}')
      else: 
        await ctx.send("What are you on ? You cant Blacklist Kaze dumbass")
  else:
    await ctx.send("Please mention the reason.")
@client.command()
@commands.has_role('STAFF TEAM')  
async def cunmute(ctx,id):
  global Mutes
  print(Mutes)
  if int(id) in Mutes:
    guild=client.get_guild(725302478823751702)
    log=guild.get_channel(802510538021011466)
    
    i=int(id)
    Mutes.remove(i)
    
    await ctx.channel.send("The User is now not blacklisted")
    await log.send(f'<@{id}> is removed from being blacklisted from confessions')
  else:
    await ctx.send('Does not work')
  
@client.command()
async def confess(ctx):
  global Mutes
  if ctx.channel.type==discord.ChannelType.private:
    if ctx.author.id not in Mutes:
    
    
      x='''<a:sleepingcat:799691148628852776> - *Do not send random, pointless messages*

  <a:sleepingcat:799691148628852776> - *Do not harass anyone*

  <a:sleepingcat:799691148628852776> - *Follow the  rules*  <#774143716042604545> 

  <a:sleepingcat:799691148628852776> - Send Your Confessions Here
  This Will Cancel Out in 30s'''
      mbed=discord.Embed(title='Type out your Confession',description=f'{x}',color=0x2f3136)
      mbed.set_footer(text='Trolling may lead to getting blacklisted from confession.')
      demand=await ctx.send(embed=mbed)
      try:
        msg=await client.wait_for(
          'message',
          timeout=30,
          check=lambda message: message.author==ctx.author and message.channel==ctx.channel
        )
        if msg:
          guild=client.get_guild(725302478823751702)
          channel=guild.get_channel(802502940606332948)
          log=guild.get_channel(802510538021011466)
          em=discord.Embed(color=0x2f3136,description=f'{msg.content}')
          em.set_author(name="F Society Confessions", icon_url='https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024')
          em.set_footer(text='Dig Bick Energy - Dm me f confess to CONFESS')
          
          e=discord.Embed(color=0x2f3136,description=f'<@{ctx.author.id}>{msg.content}')
          e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
          await channel.send(embed=em)
          await log.send(embed=e)
          await demand.delete()
      except asyncio.TimeoutError:
        await ctx.send('Cancelled',delete_after=10)
        await demand.delete()
    else:
      await ctx.send("You are muted")
  else:
    await ctx.send("I only accept confession through dms")
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=3):
  await ctx.channel.purge(limit=amount+1)
  await ctx.send(f'<a:Chat:804180442626261014> *I have deleted* {amount} *messages!*')
  await asyncio.sleep(2)
  await ctx.channel.purge(limit=amount)


@client.command(name='userinfo',aliases=['ui','UI'])
async def userinfo(ctx,member:discord.Member=None):
  if member is None:
    member=ctx.message.author 
  roles= [ role.id for role in member.roles ]
  
  badges = [public_flags for public_flags in member.public_flags]
  d={'staff':'<:staff:815232627694632980>','partner':'<:partner:815232427777720340>','bug_hunter':'<:bughunter:815188215878123530>','hypesquad_bravery':'<:HypeaSquadBravery:815187983652225064>','hypesquad_brilliance':'<:HypeSquadBrilliance:815187944675475466>','hypesquad_balance':'<:HypeSquadBalance:815187919823175721> ','early_supporter':'<:BadgeEarlySupporter:815188034655092757>','bug_hunter_level_2':'<:GoldBugHunter:815188244744372234>','verified_bot_developer':'<:EarlyVerifiedBotDeveloper:815188301707345921>','nitro':'<:nitro:815188982819848225>','boost_badges':"<a:BoostBadges:815188839487897621>"}
  s=''
  
    
  
  embed=discord.Embed(color=0x2f3136,timestamp=ctx.message.created_at)
  embed.set_author(name=f'User Info - {member}')
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f'Requested by{ctx.author}',icon_url=ctx.author.avatar_url)
  embed.add_field(name='• ID',value=f'`{member.id}` <@{member.id}>')
  embed.add_field(name='• Nickname',value=member.display_name,inline=False)
  

  
  
  for a in badges:

    if a[1] is True:
      
      s+=d[a[0]]
    
  
  b=ctx.guild.premium_subscribers
  if member in b:
    s+=d['nitro']
    s+=d['boost_badges']    
  
    embed.add_field(name='• Swaggy Server Booster',value='<@&778915337541386241> <a:nexin_pop:815257177982894091>',inline=False)
  else:
    if member.is_avatar_animated():
      s+=d['nitro']
  embed.add_field(name="• Joined at:",value=f'`{member.joined_at.strftime("%a,%#d %B %Y,%I:%M %p UTC")}`',inline=False)
  embed.add_field(name="• Created at:",value=f'`{member.created_at.strftime("%a,%#d %B %Y,%I:%M %p UTC")}`',inline=False)
  x='<a:u_Chat:790568691888029726>'
  if 788392538888601601 in roles:
    s+='<:fsociety_kul_staff:815958724329472010>'
  
  if s!='':
    embed.add_field(name='• Badges: ',value=s)
  #testingd
  else:
    embed.add_field(name='• Badges: ',value='None')
    
  
  
  await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def roles(ctx):
  x=[727404814836957236,789890292575895582,776749627248082944,803289122047393822,801780169580871690,812184488339701791,812184783496544267,812184998378602528,775985774536687636,775985579997003778,786104246051405854,799134338938699836,777459196919545856,807253618390466631,792059710589239326,803272125875617853,788392538888601601,777459196919545856]
  y=''
  for z in x:
    y+=f'<@&{z}>'
  em=discord.Embed(title="Server Hoisted Role",description=y,color=0x2f3136)   
  await ctx.send(embed=em)
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx,member:discord.Member,*,reason="No Reason Provided"):
  em=discord.Embed(title = ctx.guild.name, description= "**You have been Warned in {}!**".format(ctx.guild.name), colour=0x2f3136)
  
  icon=ctx.guild.icon_url
  em.set_footer(text="The F Society",icon_url=icon)
  em.add_field(name="Reason:",value=f"{reason}",inline=False)
  await member.send(embed=em)
  guild=client.get_guild(725302478823751702)
  await ctx.message.add_reaction("<:tickYes:815926941453385738>")
  log=guild.get_channel(774161325442072596)
  embed=discord.Embed(title='Warn log',description=f'{member} was warned by {ctx.message.author}',color=0x2f3136)
  embed.add_field(name="Reason:",value=reason)
  await log.send(embed=embed)


client.run(os.environ['DISCORD_TOKEN'])
