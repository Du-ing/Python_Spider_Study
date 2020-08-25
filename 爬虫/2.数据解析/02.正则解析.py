# 需求：爬取糗事百科中图片板块下的图片
import requests
import re
import os
# 创建一个文件夹保存爬取的图片
if not os.path.exists('./爬虫/2.数据解析/糗事百科图片'):
    os.mkdir('./爬虫/2.数据解析/糗事百科图片')

url = 'https://www.qiushibaike.com/imgrank/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
# 使用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url, headers=headers).text
# 使用聚焦爬虫将页面中所有的图片进行解析
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)

for img_src in img_src_list:
    # 拼接出一个完整的图片url
    img_src = 'https:'+img_src
    # 请求到了图片的二进制数据
    img_data = requests.get(url=img_src, headers=headers).content
    # 生成图片名称
    img_name = img_src.split('/')[-1]
    # 图片文件存储路径
    img_path = './爬虫/2.数据解析/糗事百科图片/'+img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name+'下载完成！')
