import discord
from core.any import Cog_Extension
import asyncio,random
import core.get_gpu_data as get_gpu_data

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def interval():
            rand_wait = [80,83,87,91,96,100]
            
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(971127322235260978)
            while not self.bot.is_closed():
                r,r_gpus,gpus = get_gpu_data.check()
                delay = await random.choice(rand_wait)
                if r == "on":
                    for g in gpus:
                        url = g["url"]
                        g_url = f"{g['name']}\n{url}"
                    embed = discord.Embed(title = f"上架了!!!", color = discord.Color.green())
                    embed.add_field(name=g_url,value=g["price"],inline=False)
                    await self.channel.send(embed=embed)
                elif r == "down":
                    for g in gpus:
                        url = g["url"]
                        g_url = f"{g['name']}\n{url}"
                    embed = discord.Embed(title = f"下架了QQ", color = discord.Color.red())
                    embed.add_field(name=g_url,value=g["price"],inline=False)
                    await self.channel.send(embed=embed)
                await asyncio.sleep(delay)
        self.bg_task = self.bot.loop.create_task(interval())
def setup(bot):
    bot.add_cog(Task(bot))