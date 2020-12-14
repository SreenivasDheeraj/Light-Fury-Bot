import discord
from discord.ext import commands
import json
import random
import asyncio

class Levels(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        self.bot.loop.create_task(self.save_users())

        with open(r".//users.json",'r') as f:
            self.users = json.load(f)

    ##--Randomly generate xp
    def generate_xp(self):
        return random.randint(1,3)

    def lvl_up(self,author_ID):
        next_lvl = int(self.users[author_ID]['xp'] ** (1/3))
        if( next_lvl > self.users[author_ID]['level']):
            self.users[author_ID]['level'] = next_lvl
            return True
        else:
            return False
                

    @commands.Cog.listener()
    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r".//users.json","w") as f:
                json.dump(self.users, f, indent = 4)
            await asyncio.sleep(5)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        author_ID = str(message.author.id)
        if not author_ID in self.users:
            self.users[author_ID]={}
            self.users[author_ID]['level'] = 1
            self.users[author_ID]['xp'] = 0
        xp = self.generate_xp()
        self.users[author_ID]['xp'] += xp
        print("User {} given {} xp".format(message.author.name, xp))
        if self.lvl_up(author_ID):
            embed=discord.Embed(title="Level UP! ", description=(message.author.name+" reached Level "+str(self.users[author_ID]['level'])+". Keep Going"), color=0xff00f6)
            await message.channel.send( embed = embed )
    
    @commands.command()
    async def level(self, ctx, user : discord.Member = None):
        ''' Check the level and xp of requested user'''
        user = ctx.author if not user else user
        author_ID = str(user.id)
        if not author_ID in self.users:
            await ctx.send("Requested user has no records")
        else:
            embed=discord.Embed(title = str(user.display_name), description=("Level: "+str(self.users[author_ID]['level'])+" XP: "+str(self.users[author_ID]['xp'])+". Keep Going"), color = user.color)
            await ctx.send( embed = embed )

def setup(bot):
    bot.add_cog(Levels(bot))        