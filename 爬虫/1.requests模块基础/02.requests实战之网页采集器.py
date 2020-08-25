import requests
# UA：User-Agent（请求载体的身份标识）
'''
UA检测：
    门户网站的服务器会检测对应请求的载体身份标识，
    检测到请求的载体身份标识为某一款浏览器时，
    说明这是一个正常的请求；
    但是检测到请求的载体身份标识不是某一款浏览器时，
    则为不正常的请求，服务器可能会拒绝此请求
'''
'''
UA伪装：
    爬虫对应的请求载体身份标识伪装成某一款浏览器
'''

url = "https://www.sogou.com/web"

# 输入要采集的关键词
kw = input('enter a word:')
# 处理url携带的参数：封装到字典中
param = {
    'query': kw
}
# UA伪装:将对应的User-Agent封装到字典中
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}

# 将url，请求参数和请求头信息加入到请求中
response = requests.get(url=url, params=param, headers=headers)

# 获取响应数据
page_text = response.text

# 持久化存储
fileName = './爬虫/1.requests模块基础/'+kw+'.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print(kw+'.html保存成功！')
