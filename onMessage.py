from discord.ext import commands
from discord import channel, utils
import discord
import asyncio

import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        
        if message.type == discord.MessageType.premium_guild_subscription:
            await message.channel.send('<:Boost:815188862111842334> We just Got Boosted!')
            await message.add_reaction("<a:u_crown:793089465659949076>")
count=0           
class actmsg(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        global count
        if message.channel.id == 774155081922773022:
           count+=1
        elif count==10:
            await message.channel.send("10 messages sent!")
            count=0

def setup(bot):
    bot.add_cog(BoostPlugin(bot))
def setup(bot):
    bot.add_cog(actmsg(bot))