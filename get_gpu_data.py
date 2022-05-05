from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
class GPU:
    def __init__(self,name,pn,price):
        self.name = name
        self.pn = pn
        self.price = price
op = Options()
op.add_argument("--disable-notifications")
op.add_argument("--disable-blink-features=AutomationControlled")
#op.add_argument("--headless")
op.add_experimental_option("useAutomationExtension",False)
op.add_experimental_option("excludeSwitches", ["enable-automation"])

edge = webdriver.Edge("./msedgedriver.exe",options=op)
edge.get('https://tw.evga.com/products/productlist.aspx?type=0')
time.sleep(1)
def take_gpu_info():
    gpu_info_list = edge.find_elements(By.CLASS_NAME,"grid-item")
    gpu_list = []
    for gpus in gpu_info_list:
        try:
            gpu_str = gpus.find_element(By.CLASS_NAME,"btnAddCart").accessible_name.split(', ')
            g_name = gpu_str[0].replace("Add ","")
            g_pn = gpu_str[1] .replace(" ","")
            g_price = gpus.find_element(By.CLASS_NAME,"pl-grid-price")
            gpu = GPU(g_name,g_pn,int(g_price.text.split('*')[0].replace('NT$','')
                                                            .replace(',','')
                                                            .replace('.00','')
                                                            .replace('\n','')))
            gpu_list.append(gpu)
        except:
            pass
    gpu_list.sort(key=lambda x: x.price)
    return gpu_list


gpu_list_global = []

gpu_list_global = take_gpu_info()
edge.quit()
for gpu in gpu_list_global:
    print(gpu.name)
