from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json

class Cmds(Cog_Extension):
    @commands.command()
    async def cmds(self,ctx):
        embed=discord.Embed(title="指令大全", description="以下指令在使用前請加上前綴 '['", color=discord.Color.green())
        embed.add_field(name="hello", value="輸入:[hello 後機器人跟你打招呼", inline=False)
        embed.add_field(name="shop", value="輸入:[shop 顯示EVGA官網可購買的顯示卡", inline=False)
        embed.add_field(name="search", value="輸入:[search 關鍵字 顯示可購買並符合關鍵字的顯示卡 記得[serch跟關鍵字中間有個空白鍵", inline=False)
        embed.set_footer(text="當有顯示卡上架或下架時會於[gpu-test]頻道主動通知")
        await ctx.author.send(embed=embed)
def setup(bot):
    bot.add_cog(Cmds(bot))