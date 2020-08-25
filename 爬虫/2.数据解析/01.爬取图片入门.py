# 如何爬取图片数据
import requests
img_url = 'https://pic.qiushibaike.com/system/pictures/12350/123504485/medium/XH7F1DLVN4UHI52Y.jpg'
# content返回的是二进制形式的数据
img_data = requests.get(url=img_url).content
with open('./爬虫/2.数据解析/qiutu.jpg', 'wb') as fp:
    fp.write(img_data)
print('爬取图片完成！')
