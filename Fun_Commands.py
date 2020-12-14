#######################################################################################################################################
from googlesearch import search
import asyncio
import functools
import itertools
import math
import random
import time

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions , Bot
from itertools import cycle

#######################################################################################################################################
class Fun_Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

##########################################-----Commands -----#######################################################

    ##########################################-----ping -----#######################################################
    @commands.command( name = "spam", pass_context = True) 
    async def spam(self, ctx, member: discord.Member):
        """Surprise"""
        await ctx.send("Don't Mess with the Unholy son of Lightning and Thunder !!")
        await ctx.send("!! Pay for it now !!")
        if member.id == 709422757506580521:
            member = ctx.author
        for i in range(0,100):
            await ctx.send(member.mention)
    
   
def setup(bot):
    bot.add_cog(Fun_Commands(bot))

