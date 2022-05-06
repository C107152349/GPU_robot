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
    async def serch(self,ctx,*,gpu_name):
        with open("./gpu_shop.json","r") as f:
            gpus = json.load(f)
        shop = discord.Embed(title = f"查詢結果", color = discord.Color.green())
        for g in gpus:
            if not (g["name"].find(gpu_name) == -1):
                url = g["url"]
                g_url = f"{g['name']}\n{url}"
                shop.add_field(name=g_url,value=g["price"],inline=False)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SERCH(bot))