import discord,os
from core.any import Cog_Extension,get_valid_ips,update_proxy_ips
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import asyncio,random,requests
import core.get_gpu_data as get_gpu_data
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def interval():
            await self.bot.wait_until_ready()
            subs_id_url = os.environ['subs_id_url']
            id_r = requests.get(subs_id_url)
            ids = id_r.json()
            self.channel = self.bot.get_channel(971127322235260978)
            Agent = ["Mozilla/5.0",
              "AppleWebKit/537.36",
              "Safari/537.36",
              "Gecko/20130326"]
            url = "https://tw.evga.com/products/productlist.aspx?type=0"
            valid_ips = get_valid_ips()
            while not self.bot.is_closed():
                headers = {"User-Agent":random.choice(Agent)}
                delay = 10
                if len(valid_ips) == 0:
                  update_proxy_ips(3)
                  valid_ips = get_valid_ips()
                proxy_ip = random.choice(valid_ips)
                # proxy_ip = ""
                # random_get_ip = True
                # while random_get_ip:
                #   if len(valid_ips) == 0:
                #       update_proxy_ips(3)
                #       valid_ips = get_valid_ips()
                #   try:
                #     proxy_ip = random.choice(valid_ips)
                #     requests.get('https://ip.seeip.org/jsonip?',
                #                         proxies={'http':proxy_ip,'https':proxy_ip},
                #                         timeout=10)
                #     random_get_ip = False
                #   except:
                #     valid_ips.remove(proxy_ip)
                try:
                  print("proxy ip list: ",valid_ips)
                  print("What proxy ip I use: ",proxy_ip)
                  #respose = requests.get(url=url,headers=headers)
                  respose = requests.get(url=url,headers=headers,proxies={'http':proxy_ip,'https':proxy_ip},timeout=30,verify=False)
                  print(respose)
                  r,r_gpus,gpus,time_str = get_gpu_data.check(respose)
                  delay = 110 + random.randint(-10,10)
                  if r == "on":
                    embed = discord.Embed(title = f"上架了!!!", color = discord.Color.green())
                    for g in r_gpus:
                      url = g["url"]
                      g_url = f"{g['name']}\n{url}"
                      embed.add_field(name=g_url,value=g["price"],inline=False)
                    embed.set_footer(text=time_str)
                    await self.channel.send(embed=embed)
                    for id in ids:
                      user = await self.bot.fetch_user(id)
                      await user.send(embed=embed)
                  elif r == "down":
                    embed = discord.Embed(title = f"下架了QQ", color = discord.Color.red())
                    for g in r_gpus:
                      url = g["url"]
                      g_url = f"{g['name']}\n{url}"
                      embed.add_field(name=g_url,value=g["price"],inline=False)
                    embed.set_footer(text=time_str)
                    await self.channel.send(embed=embed)
                    for id in ids:
                      user = await self.bot.fetch_user(id)
                      await user.send(embed=embed)
                  elif not r:
                    valid_ips.remove(proxy_ip)
                    delay = 5
                except:
                  delay = 5
                  valid_ips.remove(proxy_ip)
                  print("task error")
                await asyncio.sleep(delay)
        self.bg_task = self.bot.loop.create_task(interval())
def setup(bot):
    bot.add_cog(Task(bot))