import requests
import time
from bs4 import BeautifulSoup

price = 0

val = input('Введите монету\n')
val = val.upper()
url = "https://www.binance.com/api/v3/ticker/price?symbol=" + val + "USDT"

price_old = 0
int = 1

while True:
    response = requests.get(url)
    soup = str(BeautifulSoup(response.text, "html.parser"))
    # print(soup[29:36])
    time.sleep(0.1)
    price = float(soup[29:36])
    if price > price_old:
        print(int, '. ', price, '  ', '↑')
    elif price == price_old:
        print(int, '. ', price, '  ', '→')
    else:
        print(int, '. ', price, '  ', '↓')
    price_old = price
    time.sleep(9)
    int += 1
    # print(type(price[0]))
