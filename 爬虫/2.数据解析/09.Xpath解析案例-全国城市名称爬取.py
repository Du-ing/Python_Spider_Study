# 需求：爬取解析出所有城市名称
import requests
from lxml import etree
url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
fp = open('./爬虫/2.数据解析/全国城市名称.txt', 'a', encoding='utf-8')
for city_name in city_name_list:
    name = city_name.xpath('./a/text()')[0]
    fp.write(name+' ')

print('全国城市名称已爬取！')
