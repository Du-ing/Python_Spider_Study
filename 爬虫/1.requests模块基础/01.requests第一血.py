# 需求：爬取搜狗首页的页面数据
import requests
# 1.指定url
url = "https://www.sogou.com/"
# 2.发起请求，返回响应对象
response = requests.get(url=url)
# 3.获取响应数据，text返回的是字符串形式的响应数据
page_text = response.text
print(page_text)    # 输出一下
# 4.持久化存储
with open("./爬虫/1.requests模块基础/sogou.html", "w", encoding="utf-8") as fp:
    fp.write(page_text)

print("爬取页面结束！")
