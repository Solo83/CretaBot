import time
import requests
from bs4 import BeautifulSoup as Bs
import json
import os

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


id_check = 0
dva = 0

dict2 = {668: 'Active',
         669: 'Travel',
         670: 'Active',
         671: 'Comfort',
         672: 'Travel',
         673: 'Comfort',
         674: 'Travel',
         675: 'Travel',
         676: 'Active',
         677: 'Comfort',
         678: 'Active',
         679: 'Travel',
         680: 'Би-2 с чёрным салоном',
         681: 'БИ-2 с чёрным салоном',
         682: 'Style',
         706: 'Би-2 с коричневым салоном',
         707: 'Би-2 с коричневым салоном',
         731: 'Standart',
         732: 'Standart',
         741: 'Comfort',
         742: 'Travel + Advanced New с двухцветным кузовом',
         743: 'Travel + Advanced New с двухцветным кузовом',
         744: 'Travel + Advanced New с двухцветным кузовом',
         745: 'Travel + Advanced New с двухцветным кузовом',
         746: 'Travel + Advanced New с двухцветным кузовом',
         786: 'Black&Brown',
         787: 'Black&Brown с пакетом Winter',
         788: 'Black&Brown',
         789: 'Black&Brown',
         790: 'Black&Brown с пакетом Winter',
         791: 'Black&Brown с пакетом Winter',
         231: '1.6л 6MT 2WD',
         232: '1.6л 6AT 2WD',
         233: '2.0л 6AT 2WD, power: 149.6',
         234: '2.0л 6AT 4WD, power: 149.6',
         235: '1.6л 6MT 4WD',
         236: '1.6л 6AT 4WD',
         11: 'Crystal White (PGU) "Белый"',
         17: 'Sleek Silver (RHM)" "Серебристый"',
         30: 'Urban Gray (U4G)" "Темно-серый"',
         102: 'Marina Blue (N4U)" "Синий"',
         195: 'Ice Wine (W4Y)" "Светло-серый"',
         103: 'Fiery Red (R4R)" "Красный"',
         121: 'Earth Brown (P4N) "Коричневый"',
         122: 'Phantom Black (MZH) "Черный"'
         }

while dva == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    soup = Bs(requests.get(URL).content, 'html.parser').text
    dict1 = json.loads(soup)

    for item in dict1['models']:
        if item['car_id'] == 31:
            print(item['model_name'], dict2.get(item['modification_id']), "Комплектация",
                  dict2.get(item['complectation_id']), "Цвет =", dict2.get(item['color_exterior_id']), "В наличии",
                  item['count_available'], "шт.", "Цена = ", item['price'], "руб.")
            id_check += 1
        if item['modification_id'] == 233 or item['modification_id'] == 234:
            out_2L = (
                item['model_name'] + " " + str(dict2.get(item['modification_id'])) + " " + "Комплектация" + " " + str(
                    dict2.get(item['complectation_id'])) + " Цвет = " + str(
                    dict2.get(item['color_exterior_id'])) + " " + "Цена = " + str(item['price']), "руб.")
            send_telegram(out_2L)
            # dva += 1

    print()
    print("Вариантов в продаже = ", id_check)
    id_check = 0
    print()
    time.sleep(10)
