# 需求：爬取三国演义小说所有的章节标题和章节内容
import requests
from bs4 import BeautifulSoup
# 存储章节标题和章节内容的列表
title = []
detail = []
# 对首页的页面数据进行爬取
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
page_text = requests.get(url=url, headers=headers).text

# 在首页中解析出章节的标题和详情页的url
# 1. 实例化BeautifulSoup对象，需要将页面的源码数据加载到该对象中
soup = BeautifulSoup(page_text, 'lxml')
# 2. 解析章节标题和获取章节url
li_list = soup.select('.book-mulu > ul > li')
for li in li_list:
    title.append(li.a.text)     # 章节标题
    detail_url = 'https://www.shicimingju.com'+li.a['href']     # 章节url
    detail.append(detail_url)
    # 对章节详情页发起请求，解析出章节内容（选做）

# 持久化存储
with open('./爬虫/2.数据解析/三国演义.txt', 'w', encoding='utf-8') as fp:
    for i in range(len(title)):
        fp.write(title[i]+'-->'+detail[i]+'\n')

print('三国演义爬取完成！')
