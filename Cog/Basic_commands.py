#######################################################################################################################################

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
class Basic_Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
###########################################-----Events-----####################################################################
    @commands.Cog.listener()
    async def on_member_remove(self , member):
        print(f'{member} has left the server')

    @commands.Cog.listener()
    async def on_member_join(self , member):
        print(f'{member} has joined server')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if(isinstance(error, commands.CommandNotFound)):
            await ctx.send("Invalid command used")
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Please pass arguments")

##########################################-----Commands -----#######################################################

    ##########################################-----ping -----#######################################################
    @commands.command( name = "ping", pass_context = True) 
    async def ping(self, context):
        """Prints ping of the server."""
        await context.send(f"Pong! {round(self.bot.latency*1000)}ms")
    
    ###########################################-----Hello message-----#####################################################

    @commands.command(name = 'hi', pass_context = True , aliases = ['Hi','hello',"Hello"])
    async def hello_message(self, context):
        """Prints reply to any welcome message"""
        
        print('Triggered response to welcome message ')
        import random
        possibleresponses=['Hi!Glad to see you',
        'Hello!',
        'Hey there!',
        'Hey,what are you doing?',
        'Let me concentrate!!', 
        'Can you give me a call',
        'Sup',
        'Yo, whats up',
        'Nice to meet you, I was just thinking about you',
        "Hi 😊 how's the day going?"]
        await context.channel.send(random.choice(possibleresponses) + context.message.author.mention)
        return

    ###########################################-----8 ball-----#####################################################

    @commands.command(name = '8ball', pass_context = True , aliases = ["test","_ball"])
    async def eight_ball(self, context, *, qustion):
        '''8ball message generator'''
        # Imports
        import random
        print("Trigerred 8ball Reponse to", context)
        possible_responses=['As I see it, yes',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again', 
        'Don’t count on it',
        'It is certain',
        'It is decidedly so',
        'Most likely',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Outlook good',
        'Reply hazy, try again',
        'Signs point to yes',
        'Very doubtful',
        'Without a doubt',
        'Yes',
        'Yes – definitely',
        "You may rely on it"]
        await context.channel.send(random.choice(possible_responses) + context.message.author.mention)
        return

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(activity = discord.Game(next(self.bot.status)))

def setup(bot):
    bot.add_cog(Basic_Commands(bot))

