from discord.ext import commands
import discord,os
from discord.ext.commands import bot,Bot
from core.any import Cog_Extension
from core.any import get_api
import json,requests

class Hello(Cog_Extension):
    @commands.command()
    async def hello(self,ctx):
      await ctx.author.send(f"hi~~ <@{ctx.author.id}>")
def setup(bot):
    bot.add_cog(Hello(bot))