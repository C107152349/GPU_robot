from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
class Send_dm(Cog_Extension):
    @commands.command()
    async def send_dm(ctx, member: discord.Member, *, content):
        channel = await member.author.create_dm()
        await channel.send(content)
def setup(bot):
    bot.add_cog(Send_dm(bot))