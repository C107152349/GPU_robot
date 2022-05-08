from discord.ext import commands
import discord
from core.any import Cog_Extension
import re
import core.get_gpu_data as get_gpu_data
api_url = "https://api.jsonstorage.net/v1/json/92ec97f7-ba74-4070-8125-42b68701d1d0/1cbd4ab5-b572-4f60-b787-86b6c5cabe02"

class SEARCH(Cog_Extension):
    @commands.command()
    async def search(self,ctx,*,gpu_name):
        gpus = get_gpu_data.take_gpus_from_json()
        shop = discord.Embed(title = f"查詢結果", color = discord.Color.green())
        en_letter = '[\u0041-\u005a|\u0061-\u007a]+' # 大小寫英文字母
        num_letter ='[\u0030-\u0039]+'# 數字
        gpu_name_split = re.findall(num_letter,gpu_name.lower()) + re.findall(en_letter,gpu_name.lower())
        c = 0 # 符合的顯卡數目
        for g in gpus:
            e = 0
            for x in gpu_name_split:    
                if not (g["name"].lower().find(x) == -1):
                    e = e + 1
                else:
                    break
            if e == len(gpu_name_split):
                c = c + 1
                url = g["url"]
                g_url = f"{g['name']}\n{url}"
                shop.add_field(name=g_url,value=g["price"],inline=False)
        if not c > 0:
            shop.add_field(name=f"沒有可以買的{gpu_name}",value="QQ",inline=False)
        await ctx.send(embed = shop)
def setup(bot):
    bot.add_cog(SEARCH(bot))