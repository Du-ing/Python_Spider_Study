import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
site = input('请输入查询的地点：')
data = {
    'cname': '',
    'pid': '',
    'keyword': site,
    'pageIndex': '1',
    'pageSize': '10'
}

response = requests.post(url=url, data=data, headers=headers)
info = response.text
print(info)

with open("./爬虫/1.requests模块基础/KFC.txt", 'w', encoding='utf-8') as fp:
    fp.write(info)
print("爬取肯德基餐厅信息成功！")
