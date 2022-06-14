from discord.ext import commands
from discord.ext.commands import bot
import discord
from core.any import Cog_Extension
import json,os

with open('./items.json',"r",encoding="utf8") as file:
    data = json.load(file)
bot = commands.Bot(command_prefix="[")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
class ON_READY(Cog_Extension):
    @bot.event
    async def on_ready():
      status_w = discord.Status.online
      activity_w = discord.Activity(type=discord.ActivityType.watching,name="EVGA的官網",)
      await bot.change_presence(status= status_w, activity=activity_w)
      print("GPU Bot in ready")
keep_alive.keep_alive()
try:
    bot.run(data["token"])
except:
    os.system("kill 1")

