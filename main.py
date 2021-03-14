import requests
from bs4 import BeautifulSoup

url = 'https://showroom.hyundai.ru/static/js/app.js'



#soup = BeautifulSoup(full_page.content, 'html.parser')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/89.0.4389.82 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

#convert = soup.find ('div', class_ = '<text text-sm_2 dark-grey text-uppercase')
#print(soup)
#print(convert)

#for eh in convert:
#tlist = eh.find_all('div', attrs={'title':'Новая CRETA'})

