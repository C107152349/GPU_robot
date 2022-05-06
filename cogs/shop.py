from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,asyncio,datetime,random
import get_gpu_data

class SHOP(Cog_Extension):
    @commands.command()
    async def shop(self,ctx):
        with open("./gpu_shop.json","r") as f:
                    gpus = json.load(f)
        shop = discord.Embed(title = f"EVGA官網可購買的顯卡", color = discord.Color.red())
        for g in gpus:
            url = g["url"]
            g_url = f"{g['name']}\n{url}"
            shop.add_field(name=g_url,value=g["price"],inline=False)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SHOP(bot))