from bs4 import BeautifulSoup
import requests
# 将本地html文档中的数据加载到该对象中
fp = open('./爬虫/2.数据解析/test.html', 'r', encoding='utf-8')
soup1 = BeautifulSoup(fp, 'lxml')
# print(soup1)

# 获取互联网上的页面源码加载到该对象中
response = requests.get(url='https://baidu.com')
page_text = response.text
soup2 = BeautifulSoup(page_text, 'lxml')
# print(soup2)

# print(soup2.a)
# print(soup2.find('a', id='a_id'))
# print(soup2.find_all('a'))
# print(soup2.select('.mnav'))
# print(soup2.select('.tang > ul > li > a'))

# print(soup2.select('.tang > ul a')[0].text)
# print(soup2.a['href'])
