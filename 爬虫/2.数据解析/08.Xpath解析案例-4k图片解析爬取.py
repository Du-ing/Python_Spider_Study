# 需求：解析下载图片数据
import requests
from lxml import etree
url = 'http://pic.netbian.com/4kyouxi/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}

# 分页爬取
for i in range(2):
    # 第1页和其他页有区别
    if not i == 1:
        page_url = url+'index_'+str(i)+'.html'
    else:
        page_url = url

    response = requests.get(url=page_url, headers=headers)
    # 解决中文乱码
    response.encoding = response.apparent_encoding
    page_text = response.text

    # 数据解析：src属性值和alt属性值
    tree = etree.HTML(page_text)
    img_src_list = tree.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    img_name_list = tree.xpath('//ul[@class="clearfix"]/li/a/b/text()')

    for i in range(len(img_src_list)):
        # 图片rul
        img_src = 'http://pic.netbian.com'+img_src_list[i]
        # 请求获取图片二进制数据
        img_data = requests.get(url=img_src, headers=headers).content
        # 图片名称
        img_name = img_name_list[i]
        with open('./爬虫/2.数据解析/4k动漫图片/'+img_name+'.jpg', 'wb') as fp:
            fp.write(img_data)
            print(img_name+'.jpg爬取成功！')
