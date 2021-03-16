import requests
from bs4 import BeautifulSoup as Bs
import json

URL2 = 'https://showroom.hyundai.ru/rest/configurator/31/car-showroom'

soup = Bs(requests.get(URL2).content, 'html.parser').text
dict1 = json.loads(soup)


for key,value in dict1['complectations'].items():
   for x,y in value.items():
       print(x, ":" ,y)



#for key,value in dict1['modificationList'].items():
   # print (key, value)


#for key,value in dict1['exterior'].items():
  #  print(value)



