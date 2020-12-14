#######################################################################################################################################

import asyncio
import functools
import itertools
import math
import random
import time
import json
from pathlib import Path 
import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions , Bot
from itertools import cycle

###########################################-----Bot Initialisation-----#######################################################
TOKEN = "NzE1ODk0NjAxMjI3MDQyODI2.XtD8Cw.BsCVr0kRztNV8u7YJMU_4r3a0_Y"
bot = commands.Bot(command_prefix = ",")

###########################################-----Importing cogs-----####################################################################
import os
for cog in os.listdir(os.path.abspath("Cog")):
    if cog.endswith(".py"):
        try:
            cog = f"Cog.{cog.replace('.py','')}"
            bot.load_extension(cog)
            print("Loaded ",cog)
        
        except Exception as e:
            print(f"{cog} cannot be loaded")
            raise e


###########################################-----Events-----####################################################################
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle , activity = discord.Game("Havana"))
    print("Bot is ready")
    change_status.start() #background task

status = cycle(["Senorita","Bad Things","Havana"])

@tasks.loop(seconds=10)
async def change_status(self):
    await bot.change_presence(activity = discord.Game(next(self.bot.status)))

bot.run(TOKEN)
