import requests
import time
from random import randint
from bs4 import BeautifulSoup

for page in range(0, 1):  # range(0, 最后一页页码+1)
    print("当前页码：%s" % page)
    url = "https://pt.sjtu.edu.cn/subtitles.php?search=putao&page={}".format(page)
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    cookie = ""
    with requests.request('GET', url, headers={'User-agent': ua, 'cookie': cookie}) as res:
        content = res.text  # 获取HTML的内容
        time.sleep(randint(3, 5))
        soup = BeautifulSoup(content, "lxml")
        result = soup.select('a[href^="downloadsubs.php?"]')
        with open("result.txt", "w") as f:
            for item in result:
                print(item)
