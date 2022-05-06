import requests
from bs4 import BeautifulSoup 
import json
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
# }
# r = requests.get("https://tw.evga.com/products/productlist.aspx?type=0",headers=headers) #將此頁面的HTML GET下來
# soup = BeautifulSoup(r.text,"html.parser")
# sel = soup.select("div.grid-item")

def take_gpus(sel):
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
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }
    r = requests.get("https://tw.evga.com/products/productlist.aspx?type=0",headers=headers) #將此頁面的HTML GET下來
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.grid-item")
    gpus = take_gpus(sel)

    with open("./gpu_shop.json","r") as f:
        gpus_old = json.load(f)
    with open("./gpu_shop.json","w") as f:
        json.dump(gpus,f)
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
        r = "上架了!!!\n\n"
        for g in on:
            r = r + g["name"] + "\n" + str(g["price"]) + "\n\n"
        return r,gpus #回傳上架的字串r跟最新的GPU清單
    elif len(down):
        r = "下架了QQ\n\n"
        for g in down:
            r = r + g["name"] + "\n" + str(g["price"]) + "\n\n"
        return r,gpus #回傳下架的字串r跟最新的GPU清單
    else:
        return False,gpus #沒變 回傳false跟最新的GPU清單
r ,gpus = check()
if r :
    print(r)