from bs4 import BeautifulSoup
import requests

x = 0
while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = "https://news.ycombinator.com/newest" + nexx

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    teme = soup.find_all("td", class_="title")

    for temes in teme:
        temes = temes.find("a", {'class': 'storylink'})
        if temes is not None and 'github.com' in str(temes):
            sublink = temes.get('href')
            print(str(temes.text) + " " + str(sublink))
            print("_____________")

    nex = soup.find(class_='morelink')
    nexlink = nex.get('href')
    print('-_-')
    nexx = nexlink[6:]
    x = x+1