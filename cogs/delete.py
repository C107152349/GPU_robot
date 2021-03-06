from discord.ext import commands
from core.any import Cog_Extension

class Delete(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def delete(self,ctx,limit=1):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
def setup(bot):
    bot.add_cog(Delete(bot))