import requests
from bs4 import BeautifulSoup


def getUrl(urlStr):
    # 如同 Url.py
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36"}

    response = requests.get(url=urlStr, headers=headers)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    # 获取地址
    streetRestaurant = soup.find_all("a", class_="fhGHT")
    # 返回地址，叫到这个函数会获取urlStr的餐馆地址
    if streetRestaurant :
        return streetRestaurant[1].text+"\n"
