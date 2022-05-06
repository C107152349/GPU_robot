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
    GPU_shop = []   
    for s in sel:
        if s.select("input.btnAddCart"):
            t = s.select_one("input.btnAddCart")
            p = s.select_one("p.pl-grid-price strong")
            t = t["title"].split(',')
            gpu_name = t[0].replace('Add ','')
            gpu_pn = t[1].replace(' ','')
            price = int(p.text.replace(',',''))
            gpu = {
                "name" : gpu_name,
                "pn"   : gpu_pn,
                "price": price
            }
            GPU_shop.append(gpu)
    GPU_shop.sort(key=lambda x: x["price"])
    return GPU_shop
def check():
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
        return r
    elif len(down):
        r = "下架了QQ\n\n"
        for g in down:
            r = r + g["name"] + "\n" + str(g["price"]) + "\n\n"
        return r
    else:
        return False #沒變 回傳false

# r = check()
# if r :
#     print(r)

