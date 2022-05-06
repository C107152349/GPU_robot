import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import discord
from core.any import Cog_Extension
import json,os,datetime
import get_gpu_data
import time
with open('./items.json',"r",encoding="utf8") as file:
    data = json.load(file)
bot = commands.Bot(command_prefix="=")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
class ON_READY(Cog_Extension):
    @bot.event
    async def on_ready():
        print("GPU Bot in ready")
bot.run(data["token"])
