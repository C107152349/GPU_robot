import random
import requests
from bs4 import BeautifulSoup 
import json,requests,random
import discord
from fake_useragent import UserAgent
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
# }
# r = requests.get("https://tw.evga.com/products/productlist.aspx?type=0",headers=headers) #將此頁面的HTML GET下來
# soup = BeautifulSoup(r.text,"html.parser")
# sel = soup.select("div.grid-item")
api_url = "https://api.jsonstorage.net/v1/json/92ec97f7-ba74-4070-8125-42b68701d1d0/1cbd4ab5-b572-4f60-b787-86b6c5cabe02"
def take_gpus_from_json():
    req = requests.get(api_url,{
        "apiKey":"03d3f3cb-3a83-410c-b254-957ce1d31f9c"
    })
    gpus = req.json()
    return gpus
def put_gpus_to_json(gpus):
    requests.put(api_url,
        params = {"apiKey":"03d3f3cb-3a83-410c-b254-957ce1d31f9c"},
        json = gpus
    )
def take_gpus_from_EVGA(sel):
    '''
    從EVGA官網撈出可購買的顯示卡並回傳list
    '''
    GPU_shop = []   
    for s in sel:
        if s.select("input.btnAddCart"):
            t = s.select_one("input.btnAddCart")
            p = s.select_one("p.pl-grid-price strong")
            url = s.select_one("div.pl-grid-pname a")
            url = 'https://tw.evga.com/' + url["href"]
            t = t["title"].split(',')
            gpu_name = t[0].replace('Add ','')
            gpu_pn = t[1].replace(' ','')
            price = int(p.text.replace(',',''))
            gpu = {
                "name" : gpu_name,
                "pn"   : gpu_pn,
                "price": price,
                "url"  : url
            }
            GPU_shop.append(gpu)
    GPU_shop.sort(key=lambda x: x["price"])
    return GPU_shop
def check():
    '''
    假設有上架或下架，回傳上下架的字串r跟最新的GPU清單;
    假設沒變，回傳false跟最新的GPU清單。
    '''
    User_Agent = random.choice([
        "Mozilla/5.0","AppleWebKit/537.36","Safari/537.36","Gecko/20130326"])
    headers = {"User-Agent":User_Agent}
    r = requests.get(url="https://tw.evga.com/products/productlist.aspx?type=0",
                    headers=headers) #將此頁面的HTML GET下來
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.grid-item")
    if r.status_code == requests.codes.ok:
        gpus = take_gpus_from_EVGA(sel)
        #讀取儲存舊GPU資料JSON
        gpus_old = take_gpus_from_json()
        #將新的GPU資料儲存至JSON
        put_gpus_to_json(gpus)
        # with open("./gpu_shop.json","r") as f:
        #     gpus_old = json.load(f)
        # with open("./gpu_shop.json","w") as f:
        #     json.dump(gpus,f)
        on = []
        down = []
        r = ""
        for gpu in gpus:
            e = 0
            for gpu_old in gpus_old:
                if gpu["pn"] == gpu_old["pn"]:
                    e = 1
                    break
            if not e:
                on.append(gpu)
        for gpu_old in gpus_old:
            e = 0
            for gpu in gpus:
                if gpu_old["pn"] == gpu["pn"]:
                    e = 1
                    break
            if not e:
                down.append(gpu_old)
        if len(on):
            return "on",on,gpus #回傳上架的字串跟最新的GPU清單
        elif len(down):
            return "down",down,gpus #回傳下架的字串跟最新的GPU清單
        else:
            print("nothing")
            return "nothing",[],gpus #沒變 回傳false跟最新的GPU清單
    else:
        print(f'Page Error : {r.status_code}')
        return False,[],[]
r,e,gpus = check()
if r:
    print(r)
    print(e)