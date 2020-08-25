# 需求：爬取58二手房中的房源信息
import requests
from lxml import etree
# 爬取到页面源码数据
url = 'https://hf.58.com/ershoufang/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(text=page_text)
# 房名称
title_list = tree.xpath('//ul[@class="house-list-wrap"]/li//h2/a/text()')
# 房形式
type_list = tree.xpath('//ul[@class="house-list-wrap"]/li/div[2]/p[1]/span[1]/text()')
# 房面积
size_list = tree.xpath('//ul[@class="house-list-wrap"]/li/div[2]/p[1]/span[2]/text()')
fp = open('./爬虫/2.数据解析/二手房信息.txt', 'a', encoding='utf-8')
for i in range(len(title_list)):
    info = title_list[i]+'-->'+size_list[i]+type_list[i]+'\n'
    # print(info)
    fp.write(info)
print('二手房信息爬取完成！')
# 拓展：还有分页爬取
