import requests
from bs4 import BeautifulSoup

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

val = "ETH"
url = "https://www.binance.com/api/v1/depth?symbol=" + val + "USDT"
response = requests.get(url)
soup = str(BeautifulSoup(response.text, "html.parser"))
soup += "&"
# print(soup)
# print("________________")
while soup[count] != '&':
    if soup[count] == ',' and soup[count + 1] == '"' and soup[count + 2] == 'a':
        break
    else:
        count += 1
# print(count)
# print(len('{"lastUpdateId":119575240,'))
birds = str(soup[10 + 26:3142])
# print(birds)
asks = str(soup[3144 + 7:-3])
# print(asks)

count = 0
for i in range(12):
    while birds[count] != '[':
        count += 1
    m_str = birds[count + 2: count + 12]
    arr_price_green.append("{:.5f}".format(float(m_str)))
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
#
for i in range(len(arr_price_green)):
    a = float(arr_price_green[i])
    b = float(arr_price_green_2[i])
    arr_bird.append(a * b)
sum_bird = sum(arr_bird)
#
# # -----------------------------
#

count = 0
for i in range(12):
    while asks[count] != '[':
        count += 1
    m_str = asks[count + 2: count + 12]
    arr_price_red.append("{:.3f}".format(float(m_str)))
    count += 1
# print(arr_price_red)

count = 0
for i in range(len(asks)):
    if asks[count] == '"' and asks[count + 1] == ',' and asks[count + 2] == '"':
        m_str = asks[count + 3:count + 12]
        arr_price_red_2.append(m_str)
        count += 1
    else:
        count += 1
    if len(arr_price_red_2) == 12:
        break
# print(arr_price_red_2)

for i in range(len(arr_price_green)):
    a = float(arr_price_red[i])
    b = float(arr_price_red_2[i])
    arr_asks.append(a * b)
sum_asks = sum(arr_asks)

# # -----------------------------------
print('Таков стакан по валюте -', val)
print('sum_bird',sum_bird)
print('sum_asks',sum_asks)
print("------------------------------")
#
# url = "https://www.binance.com/api/v3/ticker/price?symbol=HOTETH"
# price_old = 0
# inc = 1
#
# for i in range(1, 100):
#     response = requests.get(url)
#     soup = str(BeautifulSoup(requests.get(url).text, "html.parser"))
#     # print(soup[29:36])
#     price = soup
#     print(i, price)
#     print("-------------------------------")