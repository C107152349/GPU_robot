from discord.ext import commands
import requests
from core.any import Cog_Extension,decode,get_api

class Subs(Cog_Extension):
    @commands.command()
    async def subs(self,ctx):
        apikey = decode(get_api("apikey"))
        subs_id_url = get_api("subs_id_url")
        r = requests.get(subs_id_url)
        ids = r.json()
        ids.append({"id" : ctx.author.id})
        requests.put(subs_id_url,
        params = {"apiKey":apikey},
        json = ids
        )
        await ctx.message.delete()
        await ctx.send(f"<@{ctx.author.id}> 已訂閱")
def setup(bot):
    bot.add_cog(Subs(bot))