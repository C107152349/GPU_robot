from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,requests

class Hello(Cog_Extension):
    @commands.command()
    async def hello(self,ctx):
        user = ctx.author.get_user(int(ctx.author.id))
        await ctx.send("test")
        #await ctx.send(f"hi <@{ctx.author.id}>")
def setup(bot):
    bot.add_cog(Hello(bot))