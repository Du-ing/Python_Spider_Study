import requests
import json
url = "https://movie.douban.com/j/chart/top_list"
param = {
    'type': '5',    # 电影类型
    'interval_id': '100:90',
    'action': '',
    'start': '1',   # 从哪一步电影开始取
    'limit': '20'   # 一次请求取出的电影个数
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
response = requests.get(url=url, params=param, headers=headers)

list_data = response.json()

fp = open('./爬虫/1.requests模块基础/douban_movies.json', 'w', encoding='utf-8')
json.dump(list_data, fp=fp, ensure_ascii=False)

print("爬取豆瓣电影结束！")
