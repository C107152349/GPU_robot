import requests,re,random,os,time
from discord.ext import commands
import json
# 這邊可以使用Cog功能繼承基本屬性
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def update_proxy_ips(ip_count):
  start_time = time.time()
  response = requests.get("https://www.sslproxies.org/")
  proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text)
  random.shuffle(proxy_ips)
  valid_ips = []
  count = 0
  for ip in proxy_ips:
    if (time.time() - start_time) > 90:
      break
    try:
        requests.get('https://ip.seeip.org/jsonip?',
                      proxies={'http':ip,'https':ip},
                      timeout=5)
        valid_ips.append(ip)
        count = count + 1
    except:
      pass
    if count >= ip_count:
        break
  print("new proxy ips: ",valid_ips)
  if len(valid_ips) == 0:
    valid_ips = ['']
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