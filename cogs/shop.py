from discord.ext import commands
import discord
from core.any import Cog_Extension
from core.get_gpu_data import take_gpus_from_json

class SHOP(Cog_Extension):
    @commands.command()
    async def shop(self,ctx):
        gpus,time_str = take_gpus_from_json()
        shop = discord.Embed(title = f"EVGA官網可購買的顯卡", color = discord.Color.green())
        for g in gpus:
            url = g["url"]
            g_url = f"{g['name']}\n{url}"
            shop.add_field(name=g_url,value=g["price"],inline=False)
        #await ctx.message.delete()
        shop.set_footer(text=time_str)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SHOP(bot))