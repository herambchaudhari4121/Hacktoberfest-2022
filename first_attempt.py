import requests
import time
from bs4 import BeautifulSoup

price = 0
array_price = []


val = input('Введите монету\n')
val = val.upper()
url = "https://www.binance.com/api/v3/ticker/price?symbol=" + val + "USDT"

price_old = 0
inc = 1

while True:
    while len(array_price) != 10:
        response = requests.get(url)
        soup = str(BeautifulSoup(response.text, "html.parser"))
        # print(soup[29:36])
        time.sleep(0.1)
        price = float(soup[30:36])
        array_price.append(price)
        if price > price_old:
            print(inc, '. ', price, '  ', '↑')
        elif price == price_old:
            print(inc, '. ', price, '  ', '→')
        else:
            print(inc, '. ', price, '  ', '↓')
        price_old = price
        time.sleep(5)
        inc += 1
    if (sum(array_price) / len(array_price)) > array_price[-1]:
        print('--------------------------')
        print('Aboba выросла')
        break
    elif (sum(array_price) / len(array_price)) < array_price[-1]:
        print('--------------------------')
        print('Aboba упала')
        break
    else:
        print('--------------------------')
        print('Aboba оасталась той же Абобой')
        break
