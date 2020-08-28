import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
# 代理IP
proxy = {
    'https': '1.197.204.60:9999'
}
page_text = requests.get(url=url, headers=headers, proxies=proxy).text

with open('./爬虫/4.requests模块高级/ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    print('代理完毕！')
