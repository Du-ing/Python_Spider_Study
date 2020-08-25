import requests
import json
post_url = "https://fanyi.baidu.com/sug"

# 加入UA伪装的请求头信息
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63',
}
# 输入要查找的单词
word = input("enter a word:")
# post请求携带的参数
data = {
    'kw': word
}
# 发送post请求
response = requests.post(url=post_url, data=data, headers=headers)
# 获取响应数据，json()方法返回的是一个json对象
json_obj = response.json()
print(json_obj)

# 持久化存储
fp = open('./爬虫/1.requests模块基础/'+word+'.json', 'w', encoding='utf-8')
json.dump(json_obj, fp=fp, ensure_ascii=False)

print('查询结束！')
