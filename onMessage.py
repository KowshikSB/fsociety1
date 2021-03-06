import discord
import os
import re
import cogs
import discord.utils

from urllib.parse import urlparse
from discord.colour import Color
from discord.ext import commands



'''Module for server commands.'''


class Server:

    def __init__(self, bot):
        self.bot = bot
        self.invites = ['discord.gg/', 'discordapp.com/invite/']
        self.invite_domains = ['discord.gg', 'discordapp.com']

    def find_server(self, msg):
        server = None
        if msg:
            try:
                float(msg)
                server = self.bot.get_guild(int(msg))
                if not server:
                    return self.bot.bot_prefix + 'Server not found.', False
            except:
                for i in self.bot.guilds:
                    if i.name.lower() == msg.lower().strip():
                        server = i
                        break
                if not server:
                    return self.bot.bot_prefix + 'Could not find server. Note: You must be a member of the server you are trying to search.', False

        return server, True

    # Stats about server
    @commands.group(aliases=['server', 'sinfo', 'si'], pass_context=True, invoke_without_command=True)
    async def serverinfo(self, ctx, *, msg=""):
        """Various info about the server. [p]help server for more info."""
        if ctx.invoked_subcommand is None:
            if msg:
                server = None
                try:
                    float(msg)
                    server = self.bot.get_guild(int(msg))
                    if not server:
                        return await ctx.send(
                                              self.bot.bot_prefix + 'Server not found.')
                except:
                    for i in self.bot.guilds:
                        if i.name.lower() == msg.lower():
                            server = i
                            break
                    if not server:
                        return await ctx.send(self.bot.bot_prefix + 'Could not find server. Note: You must be a member of the server you are trying to search.')
            else:
                server = ctx.message.guild

            online = 0
            for i in server.members:
                if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                    online += 1
            all_users = []
            for user in server.members:
                all_users.append('{}#{}'.format(user.name, user.discriminator))
            all_users.sort()
            all = '\n'.join(all_users)

            channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])

            role_count = len(server.roles)
            emoji_count = len(server.emojis)

            
            em = discord.Embed(color=0xea7938)
            em.add_field(name='Name', value=server.name)
            em.add_field(name='Owner', value=server.owner, inline=False)
            em.add_field(name='Members', value=server.member_count)
            em.add_field(name='Currently Online', value=online)
            em.add_field(name='Text Channels', value=str(channel_count))
            em.add_field(name='Region', value=server.region)
            em.add_field(name='Verification Level', value=str(server.verification_level))
            
            em.add_field(name='Number of roles', value=str(role_count))
            em.add_field(name='Number of emotes', value=str(emoji_count))
            
            
            
            em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.set_thumbnail(url=server.icon_url)
            em.set_author(name='Server Info', icon_url='https://i.imgur.com/RHagTDg.png')
            em.set_footer(text='Server ID: %s' % server.id)
            await ctx.send(embed=em)
           
            await ctx.message.delete()

    @serverinfo.command(pass_context=True)
    async def emojis(self, ctx, msg: str = None):
        """List all emojis in this server. Ex: [p]server emojis"""
        if msg:
            server, found = self.find_server(msg)
            if not found:
                return await ctx.send(server)
        else:
            server = ctx.message.guild
        emojis = [str(x) for x in server.emojis]
        b=""
        for x in emojis:
            b+=x
        em=discord.Embed(title="Emoji List",description=x,Color=0x2f3136)
        await ctx.send(embed=em)
        await ctx.message.delete()

    
    
    @commands.command(aliases=['invitei', 'ii'], pass_context=True)
    async def inviteinfo(self, ctx, *, invite: str = None):
        """Shows invite information."""
        if invite:
            for url in re.findall(r'(https?://\S+)', invite):
                try:
                    invite = await self.bot.get_invite(urlparse(url).path.replace('/', '').replace('<', '').replace('>', ''))
                except discord.NotFound:
                    return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                break
        else:
            async for msg in ctx.message.channel.history():
                if any(x in msg.content for x in self.invites):
                    for url in re.findall(r'(https?://\S+)', msg.content):
                        url = urlparse(url)
                        if any(x in url for x in self.invite_domains):
                            print(url)
                            url = url.path.replace('/', '').replace('<', '').replace('>', '').replace('\'', '').replace(')', '')
                            print(url)
                            try:
                                invite = await self.bot.get_invite(url)
                            except discord.NotFound:
                                return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                            break
                
        if not invite:
            return await ctx.send(self.bot.bot_prefix + "Couldn't find an invite in the last 100 messages. Please specify an invite.")
        
        data = discord.Embed()
        content = None
        if invite.id is not None:
            content = self.bot.bot_prefix + "**Information about Invite:** %s" % invite.id
        if invite.revoked is not None:
            data.colour = discord.Colour.red() if invite.revoked else discord.Colour.green()
        if invite.created_at is not None:
            data.set_footer(text="Created on {} ({} days ago)".format(invite.created_at.strftime("%d %b %Y %H:%M"), (invite.created_at - invite.created_at).days))
        if invite.max_age is not None:
            if invite.max_age > 0:
                expires = '%s s' % invite.max_age
            else:
                expires = "Never"
            data.add_field(name="Expires in", value=expires)
        if invite.temporary is not None:
            data.add_field(name="Temp membership", value="Yes" if invite.temporary else "No")
        if invite.uses is not None:
            data.add_field(name="Uses", value="%s / %s" % (invite.uses, invite.max_uses))
        if invite.inviter.name is not None:
            data.set_author(name=invite.inviter.name + '#' + invite.inviter.discriminator + " (%s)" % invite.inviter.id, icon_url=invite.inviter.avatar_url)

        if invite.guild.name is not None:
            data.add_field(name="Guild", value="Name: " + invite.guild.name + "\nID: %s" % invite.guild.id, inline=False)
        if invite.guild.icon_url is not None:
            data.set_thumbnail(url=invite.guild.icon_url)

        if invite.channel.name is not None:
            channel = "%s\n#%s" % (invite.channel.mention, invite.channel.name) if isinstance(invite.channel, discord.TextChannel) else invite.channel.name
            data.add_field(name="Channel", value="Name: " + channel + "\nID: %s" % invite.channel.id, inline=False)

        try:
            await ctx.send(content=content, embed=data)
        except:
            await ctx.send(content="I need the `Embed links` permission to send this")


def setup(bot):
    bot.add_cog(Server(bot))