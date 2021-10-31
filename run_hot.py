import requests
from bs4 import BeautifulSoup
import os

count = 0
birds = ''
asks = ''
arr_bird = []
arr_asks = []
arr_price_green = []
arr_price_green_2 = []
arr_price_red = []
arr_price_red_2 = []
sum_bird = 0
sum_asks = 0

val = "HOT"
url = "https://www.binance.com/api/v1/depth?symbol=" + val + "ETH"
response = requests.get(url)
soup = str(BeautifulSoup(response.text, "html.parser"))
soup += "&"
# print(soup)
# print("________________")

while soup[count] != '&':
    if soup[count] == ',' and soup[count+1] == '"' and soup[count+2] == 'a':
        break
    else:
        count += 1
birds = str(soup[7 + 27:3289]) + ']&'
# print(birds)
asks = str(soup[3291+8:-3]) + ']&'



count = 0
for i in range(12):
    while birds[count] != '[':
        count += 1
    m_str = birds[count + 2: count + 12]
    arr_price_green.append("{:.8f}".format(float(m_str)))
    count += 1
# print(arr_price_green)

count = 0
for i in range(len(birds)):
    if birds[count] == '"' and birds[count + 1] == ',' and birds[count + 2] == '"':
        m_str = birds[count + 3:count + 12]
        arr_price_green_2.append(m_str)
        count += 1
    else:
        count += 1
    if len(arr_price_green_2) == 12:
        break
# print(arr_price_green_2)

for i in range(len(arr_price_green)):
    a = float(arr_price_green[i])
    b = float(arr_price_green_2[i])
    arr_bird.append(a * b)
sum_bird = sum(arr_bird)

# -----------------------------


count = 0
for i in range(12):
    while asks[count] != '[':
        count += 1
    m_str = asks[count+2: count+12]
    arr_price_red.append("{:.8f}".format(float(m_str)))
    count += 1
# print(arr_price_green)

count = 0
for i in range(len(asks)):
    if asks[count] == '"' and asks[count+1] == ',' and asks[count+2] == '"':
        m_str = asks[count+3:count+12]
        arr_price_red_2.append(m_str)
        count += 1
    else:
        count += 1
    if len(arr_price_red_2) == 12:
        break
# print(arr_price_green_2)

for i in range(len(arr_price_green)):
    a = float(arr_price_red[i])
    b = float(arr_price_red_2[i])
    arr_asks.append(a * b)
sum_asks = sum(arr_asks)

# -----------------------------------
# print(sum_bird)
# print(sum_asks)
print("------------------------------")

url = "https://www.binance.com/api/v3/ticker/price?symbol=HOTETH"
price_old = 0
inc = 1

response = requests.get(url)
soup = str(BeautifulSoup(requests.get(url).text, "html.parser"))
print('Текущий курс по монете -', soup[28:38])
price = float(soup[28:38])

print("-------------------------------")
answer = int(input('Вы собираетесь покупать монеты или же хотите продать?\n1 - покупка, 2 - продажа,3 - получить совет, 4 - выход\n'))
os.system('cls')
print("Данная программа не покупает и не продает никакие валюты, а лишь просчитывает возможный курс после возможной транзакции.\nНаша организация ответственности за ущер и крах не несет. Спасибо, что выбираете 'SiBears New'!")
c = price
if answer == 1:
    k = sum_bird
    n = int(input("Введите ваш возможный баланс, на который вы хотите закупить монету Money\n"))
    for i in range(10):
        c = c * (1 - k / (k + c * n / 10)) + c
        print(i, c)
    print("Курс изменится на такой", "{:.10f}".format(float(c)), 'после вашего возможного трейда')
elif answer == 2:
    k = sum_asks
    n = int(input("Введите вашу возможную сумму на которую вы хотите продать монеты(монету) Money\n"))
    for i in range(10):
        c = (k / (k + c * n / 10)) * c
        c1 = "{:.8f}".format(float(c))
        # print(i, c1)
    print("Курс изменится на такой", c1, 'после вашего возможного трейда')
elif answer == 3:
    os.system('info.py')
elif answer == 4:
    exit()
print('Хотите начать все сначала? Тогда нажмите 1, иначе любую другую клавишу')
answer = int(input())
if answer == 1:
    os.system('start_programm.py')
