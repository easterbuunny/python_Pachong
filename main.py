import Url

# 主函数
if __name__ == '__main__':
    # 网页链接如同下面
    # https://www.tripadvisor.fr/Restaurants-g187147-c27-Paris_Ile_de_France.html

    # 获取部分链接
    urlChinois = "Restaurants-g187147-c11-Paris_Ile_de_France.html"
    Url.getUrl(urlChinois)

    # 可以添加 其他餐馆 格式一定是如同上面


# 结果在同一个文件夹里 名为 restaurant.txt
