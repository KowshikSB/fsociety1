from discord.colour import Color
from discord.ext import commands
from discord import client, utils
import discord
import asyncio
from discord.ext import tasks
from discord.ext.commands.core import check
from discord.utils import get 

from discord.ext.commands.converter import clean_content
client = commands.Bot(command_prefix =commands.when_mentioned_or('f ','F '),intents=discord.Intents.all())


command_prefix =commands.when_mentioned_or('f ')


class onMessage(commands.Cog):
	def __init__(self, bot):
		self.client = bot
	
		x='<:h_:788652894227267584><:e_:788652806235488256><:l_:788653083005157396><:p_:788654650374225930> <:d_:788651820054609930><:e_:788652806235488256><:s_:788653491492880414> <:k_:788653044950237194>'
		y='''*You can use modmail for any of the following reasons*
<a:tickup:774207637184839680> *Question your moderation infraction*
<a:tickup:774207637184839680> *Reporting any user in the server*
<a:tickup:774207637184839680> *Just ask a general question!*
If you want to contact Mod. Send your query now. 
Mods Will be notified. If you opened this by mistake 
Use **f close** to Close the Ticket'''

		em=discord.Embed(title=x,description=y,colour = 0x2f3136)
		em.set_thumbnail(url='https://cdn.discordapp.com/icons/725302478823751702/a_98429fc81380f70cbb78548bccf3d70e.gif?size=1024')
		em.set_footer(text="The F Society")
		
		@commands.Cog.listener()
		async def on_message(self, message):
			if message.author.bot:
				return
			
				
			await client.wait_for('f support',timeout=60,check=check)
			if isinstance(message.channel, discord.DMChannel):
				await message.send(embed=em)
				guild = self.client.get_guild(725302478823751702)
				categ = utils.get(guild.categories, name = "Modmail tickets")
				if not categ:
					overwrites = {
						guild.default_role : discord.PermissionOverwrite(read_messages = False),
						guild.me : discord.PermissionOverwrite(read_messages = True)
					}
					categ = await guild.create_category(name = "Modmail tickets", overwrites = overwrites)

				channel = utils.get(categ.channels, topic = str(message.author.id))
				if not channel:
					channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topic = str(message.author.id))
					await channel.send(f"New modmail created by {message.author.mention}")

				embed = discord.Embed(description = message.content, colour = 0x2f3136)
				embed.set_author(name = message.author, icon_url = message.author.avatar_url)
				await channel.send(embed = embed)

			elif isinstance(message.channel, discord.TextChannel):
				if message.content.startswith(self.client.command_prefix):
					pass
				else:
					topic = message.channel.topic
					if topic:
						member = message.guild.get_member(int(topic))
						if member:
							embed = discord.Embed(description = message.content, colour = 0x2f3136)
							embed.set_author(name = message.author, icon_url = message.author.avatar_url)
							await member.send(embed = embed)

		@commands.command()
		async def close(self, ctx):
			if ctx.channel.category.name == "Modmail tickets":
				await ctx.send("Deleting the channel in 10 seconds!")
				await asyncio.sleep(10)
				await ctx.channel.delete()

def setup(bot):
	bot.add_cog(onMessage(bot))
@client.event
async def on_message(message): 
  if message in ['boost','Boost','BOOST']:
    x='''<a:boost_us:813756354166128660> 1 Boost  - 
• *Custom Color Role of your Choice*
• *Unlocks a private chat room* <#799319127515988029>
•  *Leveling System Perks Bypass*
•  *Unlocks* <#778843597528891392>
•  *Unlocks Cute Secret Emojis Packs*

 <a:boost_us:813756354166128660> 2 Boosts -
 • *Gets a Custom hoisted role until the Boost lasts*

 <a:boost_us:813756354166128660> More Than 2 Boosts -
• *Custom Private VC*

Dm <@261742964441612298> To get the perks.'''
    em=discord.Embed(title='Boost Us <a:b_capoo_heartlove:813626091159027742>',description=x,color=0x2f3136)
    em.set_thumbnail(url=message.guild.icon_url)
    await message.channel.trigger_typing()
    await asyncio.sleep(2)
    await message.send(embed=em)
