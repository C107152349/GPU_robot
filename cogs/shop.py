from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,asyncio,datetime,random,requests
import get_gpu_data
api_url = "https://api.jsonstorage.net/v1/json/92ec97f7-ba74-4070-8125-42b68701d1d0/1cbd4ab5-b572-4f60-b787-86b6c5cabe02"

class SHOP(Cog_Extension):
    @commands.command()
    async def shop(self,ctx):
        req = requests.get(api_url,{
            "apiKey":"03d3f3cb-3a83-410c-b254-957ce1d31f9c"
        })
        gpus = req.json()
        shop = discord.Embed(title = f"EVGA官網可購買的顯卡", color = discord.Color.red())
        for g in gpus:
            url = g["url"]
            g_url = f"{g['name']}\n{url}"
            shop.add_field(name=g_url,value=g["price"],inline=False)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SHOP(bot))