from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json,asyncio,datetime,random
import get_gpu_data

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(971127322235260978)
            while not self.bot.is_closed():
                r,gpus = get_gpu_data.check()
                if r:
                    await self.channel.send(r)
                await asyncio.sleep(90)
        self.bg_task = self.bot.loop.create_task(interval())
def setup(bot):
    bot.add_cog(Task(bot))