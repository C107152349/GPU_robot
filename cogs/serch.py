from http.cookiejar import Cookie
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,requests
import get_gpu_data
api_url = "https://api.jsonstorage.net/v1/json/92ec97f7-ba74-4070-8125-42b68701d1d0/1cbd4ab5-b572-4f60-b787-86b6c5cabe02"

class SERCH(Cog_Extension):
    @commands.command()
    async def serch(self,ctx,*,gpu_name):
        req = requests.get(api_url,{
            "apiKey":"03d3f3cb-3a83-410c-b254-957ce1d31f9c"
        })
        gpus = req.json()
        shop = discord.Embed(title = f"查詢結果", color = discord.Color.green())
        e = 0
        for g in gpus:
            if not (g["name"].find(gpu_name) == -1):
                url = g["url"]
                g_url = f"{g['name']}\n{url}"
                shop.add_field(name=g_url,value=g["price"],inline=False)
                e = 1
        if not e:
            shop.add_field(name=f"沒有可以買的{gpu_name}",value="QQ",inline=False)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SERCH(bot))