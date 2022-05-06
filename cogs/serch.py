from http.cookiejar import Cookie
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json
import get_gpu_data
with open('./items.json', 'r', encoding='utf8') as file:
   data = json.load(file)

class SERCH(Cog_Extension):
    @commands.command()
    async def serch(self,ctx,gpu_name):
        r = get_gpu_data.check()
        if r :
            await ctx.send(f"{r}")
def setup(bot):
    bot.add_cog(SERCH(bot))