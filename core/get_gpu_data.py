from bs4 import BeautifulSoup 
import json,requests,random,time
import os
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
# }
# r = requests.get("https://tw.evga.com/products/productlist.aspx?type=0",headers=headers) #將此頁面的HTML GET下來
# soup = BeautifulSoup(r.text,"html.parser")
# sel = soup.select("div.grid-item")
def take_gpus_from_json():
    gpus_url = os.environ['gpu_url']
    req = requests.get(gpus_url)
    gpus = req.json()
    return gpus[1:], gpus[0]
def put_gpus_to_json(gpus):
    apikey = os.environ['apikey']
    gpus_url = os.environ['gpu_url']
    requests.put(gpus_url,
        params = {"apiKey":apikey},
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
def check(r):
    '''
    假設有上架或下架，回傳上下架的字串r跟最新的GPU清單;
    假設沒變，回傳false跟最新的GPU清單。
    '''
    # User_Agent = random.choice([
    #     "Mozilla/5.0","AppleWebKit/537.36","Safari/537.36","Gecko/20130326"])
    # headers = {"User-Agent":User_Agent}
    # r = rs.get(url="https://tw.evga.com/products/productlist.aspx?type=0",
    #                 headers=headers)
    # r = requests.get(url="https://tw.evga.com/products/productlist.aspx?type=0",
    #                 headers=headers) #將此頁面的HTML GET下來
    time_struct = time.localtime(time.time())
    time_str = "更新時間 : " + str(time_struct.tm_year) + "年" +str(time_struct.tm_mon) + "月" + str(time_struct.tm_mday) + "日" + str(time_struct.tm_hour) + ":" + str(time_struct.tm_min)+":"+str(time_struct.tm_sec)
    try:
      soup = BeautifulSoup(r.text,"html.parser")
      sel = soup.select("div.grid-item")
      if r.status_code == requests.codes.ok and sel:
          gpus = take_gpus_from_EVGA(sel)
          #讀取儲存舊GPU資料JSON
          
          gpus_old,time_old = take_gpus_from_json()
          gpus.insert(0,time_str)
          #將新的GPU資料儲存至JSON
          
          put_gpus_to_json(gpus)
          on = []
          down = []
          
          for gpu in gpus[1:]:
              e = 0
              for gpu_old in gpus_old:
                  if gpu["pn"] == gpu_old["pn"]:
                      e = 1
                      break
              if not e:
                  on.append(gpu)
          
          for gpu_old in gpus_old:
              e = 0
              for gpu in gpus[1:]:
                  if gpu_old["pn"] == gpu["pn"]:
                      e = 1
                      break
              if not e:
                  down.append(gpu_old)
          if len(on):
              print(f"{ r.status_code} on")
              return "on",on,gpus[1:],time_str #回傳上架的字串跟最新的GPU清單
          elif len(down):
              print(f"{ r.status_code} down")
              return "down",down,gpus[1:],time_str #回傳下架的字串跟最新的GPU清單
          else:
              print(f"{ r.status_code} nothing")
              return "nothing",[],gpus[1:],time_str #沒變 回傳false跟最新的GPU清單
      else:
          print(soup)
          print(f'Page Error : {r.status_code}')
          return False,[],[],time_str
    except:
      print("check error")
      return False,[],[],time_str