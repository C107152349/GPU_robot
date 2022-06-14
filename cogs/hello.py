from discord.ext import commands
from core.any import Cog_Extension

class Hello(Cog_Extension):
    @commands.command()
    async def hello(self,ctx):
      await ctx.author.send(f"hi~~ <@{ctx.author.id}>")
def setup(bot):
    bot.add_cog(Hello(bot))