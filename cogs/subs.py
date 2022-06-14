from discord.ext import commands
import requests,os
from core.any import Cog_Extension

class Subs(Cog_Extension):
    @commands.command()
    async def subs(self,ctx):
        now_id = ctx.author.id
        apikey = os.environ['apikey']
        subs_id_url = os.environ['subs_id_url']
        r = requests.get(subs_id_url)
        ids = r.json()
        e = 0
        for id in ids:
          if id == now_id:
            e = 1
            break
        if not e:
          ids.append(now_id)
          requests.put(subs_id_url,
          params = {"apiKey":apikey},
          json = ids
          )
          await ctx.author.send(f"<@{now_id}> 已訂閱")
          print(ctx.author,"已訂閱")
        else:
          await ctx.author.send("您訂閱過囉!")
def setup(bot):
    bot.add_cog(Subs(bot))