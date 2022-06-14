from discord.ext import commands
import discord,os
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,requests

class Send_dm(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def send_dm(self,ctx):
        subs_id_url = os.environ['subs_id_url']
        id_r = requests.get(subs_id_url)
        ids = id_r.json()
        for id in ids:
          user = await ctx.bot.fetch_user(id)
          await user.send(f"hi <@{user.id}>")
def setup(bot):
    bot.add_cog(Send_dm(bot))