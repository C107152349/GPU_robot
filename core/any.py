import discord
from discord.ext import commands
import json
# 這邊可以使用Cog功能繼承基本屬性
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
def encode(string):
    '''
    將輸入的字串進行編碼
    '''
    e = ""
    for s in string:
        e = e + (chr(ord(s) + 1))
    return e
def decode(string):
    '''
    將輸入的字串進行解碼
    '''
    d = ""
    for s in string:
        d = d + (chr(ord(s) - 1))
    return d
def get_api(d:str):
    """
    輸入字串回傳該api
    """
    with open('./jsonstorage.json',"r",encoding="utf8") as file:
        data = json.load(file)
    return data[d]