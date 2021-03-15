import time
import requests
from bs4 import BeautifulSoup as Bs
import json

URL = 'https://showroom.hyundai.ru/rest/car'



def send_telegram(text: str):
    token = "1660802141:AAHedSPBsDHGnYCvh6bVOpnTKbxzAelk5xE"
    url = "https://api.telegram.org/bot"
    channel_id = "421965977"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

id = 0
dva = 0

while dva==0:

 soup = Bs(requests.get(URL).content, 'html.parser').text
 dict1 = json.loads(soup)

 for item in dict1['models']:
    if item['car_id'] == 31:
        print(item['model_name'], item['modification_id'],"Комплектация", item['complectation_id'], "Цена = ", item['price'])
        id += 1
    if item['modification_id'] == 233 or item['modification_id'] == 234:
        str1 = (item['model_name'] + " " + str(item['modification_id']) + " " + "Комплектация" + " " + str(item['complectation_id']) + " " + "Цена = " + str(item['price']))
        send_telegram(str1)
        dva += 1

 print()
 print("Крет в продаже = ", id)
 id=0
 print()
 time.sleep(10)



