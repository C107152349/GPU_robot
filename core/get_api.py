import requests,json
from core import ende

def get_api(d:str):
    """
    輸入字串回傳該api
    """
    with open('./jsonstorage.json',"r",encoding="utf8") as file:
        data = json.load(file)
    return data[d]