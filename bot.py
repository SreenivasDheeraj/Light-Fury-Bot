"""The bot"""

import asyncio
import aiohttp
from datetime import datetime, timedelta
import discord
from discord.ext import commands
import importlib
from modules.utils import utils
import os
import sys


PREFIX = ','

bot = commands.Bot(command_prefix = ",")

for cog in os.listdir(os.path.abspath("modules")):
    if cog.endswith(".py"):
        try:
            cog = f"modules.{cog.replace('.py','')}"
            bot.load_extension(cog)
            print("Loaded ",cog)
        
        except Exception as e:
            print(f"{cog} cannot be loaded")
            raise e


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

bot.run("NzE3MzkyNzIwMTA0MjU5NjE0.XtZqLg.ChRLy7LuhArMNo2bNLenkZq2LYs", reconnect=True)

