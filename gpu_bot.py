from typing_extensions import runtime
from discord.ext import commands
import discord
import json

with open('./items.json',"r",encoding="utf8") as file:
    data = json.load(file)
bot = commands.Bot(command_prefix="=")


@bot.event
async def on_ready():
    print("GPU Bot in ready")
@bot.command()
async def hello(ctx):
    await ctx.send(f"hi <@{ctx.author.id}>")
@bot.command()
async def serch(ctx,gpu_name):
    await ctx.send(f"{gpu_name}")
bot.run(data["token"])
