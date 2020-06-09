import asyncio
import functools
import itertools
import math
import random
import time

import discord
from async_timeout import timeout
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions 
from itertools import cycle

class Mod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

##########################################-----Kick-----#################################################################

    @commands.command( name = 'kick', pass_context = True )
    @commands.has_permissions( kick_members = True )
    async def kick( self, context , user:discord.Member , * , reasons = None ):
        """Kicks the user if has permissions to do so"""
        try:
            if reasons == None:
                reasons = "no reason :person_shrugging:"
            await user.kick(reason = reasons)
            embed = discord.Embed(title = "User Kicked!", description = ("**"+user.mention+"** was kicked by **"+str(context.message.author.mention)+"** because "+reasons).format(user, context.message.author), color=0xff00f6)
            await context.send(embed = embed)
            await user.send(embed = embed)
        except discord.Forbidden:
            await context.send("Nice try but you do not have permission qt :stuck_out_tongue_winking_eye:"+context.message.author.mention)
        
        return

############################################-----Ban a user--- --#######################################################

    @commands.command(name = 'ban',pass_context=True)
    @commands.has_permissions(ban_members = True)
    async def ban(self , context , user:discord.Member , * , reasons=None ):
        """Kicks the user if has permissions to do so"""
        if reasons == None:
            reasons = "no reason :person_shrugging:"
        await user.ban(reason = reasons)
        embed=discord.Embed(title="User banned!", description=("**"+user.mention+"** was banned by **"+str(context.message.author.mention)+"** because "+reasons).format(user, context.message.author), color=0xff00f6)
        await context.send( embed = embed )
        await user.send( embed = embed )

############################################-------Clear Messages------#######################################################

    @commands.command(name = "clear", pass_context = True )
    @commands.has_permissions(manage_messages = True)
    async def clear(self , context, amount = 5 ):
        '''Delete a specified number of(default : 5) messages from server.'''
        await context.channel.purge( limit=amount)
        print(f"Cleared {amount} meassages") 

##########################################-----Unban a member-----################################################################
    @commands.command(name = "unban" , pass_context = True)
    async def unban(self , context , * , member ):
        '''Unban a user.
        Should be of the format membername#discriminator code Ex: unban Abc#XXXX
        '''
        banned_users = await context.guild.bans()
        member_name , member_discriminator = member.split('#')
        #Should be of the format membername#discriminator code Ex: unban Shiki Brekksten#7042
        for ban_entry in banned_users:
            user = ban_entry.user
            if( user.name , user.discriminator ) == ( member_name, member_discriminator ):
                await context.guild.unban(user)
                print(f"Unbanned {user.name}#{user.discriminator}")
                await context.send(f"Unbanned {user.name}#{user.discriminator}")
                return 

def setup(bot):
    bot.add_cog(Mod(bot))