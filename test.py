import requests
from bs4 import BeautifulSoup as Bs
import json

URL2 = 'https://showroom.hyundai.ru/rest/configurator/31/car-showroom'

soup = Bs(requests.get(URL2).content, 'html.parser').text
dict1 = json.loads(soup)
new_dict = {}


for item in dict1['complectations']:
     print(dict1['complectations'].get(item).values())

for item in dict1['modificationList']:
    print(dict1['modificationList'].get(item).values())




