import discord,requests,re,random,os
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
def update_proxy_ips(ip_count):
  response = requests.get("https://www.sslproxies.org/")
  proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text)
  random.shuffle(proxy_ips)
  valid_ips = []
  count = 0
  for ip in proxy_ips:
      try:
          requests.get('https://ip.seeip.org/jsonip?',
                        proxies={'http':ip,'https':ip},
                        timeout=10)
          valid_ips.append(ip)
          count = count + 1
      except:
        pass
      if count >= ip_count:
          break
  print("new proxy ips: ",valid_ips)
  proxy_ips_url = os.environ['proxy_ips_url']
  apiKey = os.environ['apikey']
  requests.put(url=proxy_ips_url,
              params={"apiKey":apiKey},
              json=valid_ips)
def get_valid_ips():
    try:
        proxy_ips_url = os.environ['proxy_ips_url']
        response = requests.get(proxy_ips_url)
        return response.json()
    except:
        return []