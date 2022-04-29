from requests import get
from bs4 import BeautifulSoup

import FileRead
import FileWrite
import StreetRestaurant


def getUrl(urlStr):
    # 原网站
    url = "https://www.tripadvisor.fr/"
    # 反扒机制 貌似没什么用，但是以防万一
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36"}

    # 获取网页数据
    response = get(url=url + urlStr, headers=headers)
    # 如有中文，原文会是你以为的乱码，这一行会防止乱码，正常现实
    response.encoding = response.apparent_encoding

    # 爬虫框架，来获取网页源码，有些反爬机制获取不了全部的源码，储存框架为soup变量方便使用
    soup = BeautifulSoup(response.text, "html.parser")

    # 用soup(上一个)获取HTML 源码里的餐馆名字，获取列表，储存在nomRestaurant 变量
    nomRestaurant = soup.find_all("a", class_="bHGqj Cj b")

    # 查询列表的的每一个储存在restaurant 变量
    for restaurant in nomRestaurant:
        # 餐馆名字前面有序号 用split 分开来成列表
        # splitNum[0] 序号， splitNum[1] 餐馆名字
        splitNum = restaurant.text.split(".")
        # 获取地址，餐馆链接里面 另外又叫了 StreetRestaurant 函数 获取单独地址
        adr = StreetRestaurant.getUrl(url + restaurant.get('href'))
        b = False
        # 查询餐厅名字和地址是否有重复 (japonais, chinois, ...) 有些两个标签里都有这家餐馆
        # 阅读文件，将每一行加入列表中
        for listResto in FileRead.reader("restaurant.txt").readlines():
            # 每一行有"tabulation" 隔开餐馆名字喝地址
            splitResto = listResto.split("\t\t")
            # 检查是否有同名同地址一处存过在文件里面
            if splitResto[0] == splitNum[1] and splitResto[1] == adr:
                # 如有相同就停止循环(for)
                b = True
                print(splitResto[0] + "\t" + splitResto[1] + " le restaurant existe déjà.")
                break
            else:
                # 如果没有找到相同的就继续循环
                pass
        # 如果没有停止循环就是没有相同餐馆名字喝地址
        if not b:
            print(splitNum[1] + " est ajouté.")
            # 写入文件
            FileWrite.writer("restaurant.txt", splitNum[1] + "\t\t" + adr)

    # 命令板 阅读中的网页
    print(response.url)
    # HTML 查找下一页
    nextPage = soup.find_all("link", rel="next")
    # 如有下一页就重复前面的操作在下一页，如果没有就结束
    if nextPage:
        getUrl(nextPage[0].get('href'))
