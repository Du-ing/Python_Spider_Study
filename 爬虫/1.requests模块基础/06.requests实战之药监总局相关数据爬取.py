import requests
import json
# 批量获取不同企业的id值
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}
id_list = []    # 存储企业id
json_ids = requests.post(url=url, data=data, headers=headers).json()
# 从json字典中解析出所有企业的id
for dic in json_ids['list']:
    id_list.append(dic['ID'])
print(id_list)

# 用企业id获取企业详情数据
with open('./爬虫/1.requests模块基础/enterprise.json', 'w', encoding='utf-8') as fp:
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data1 = {
            'id': id
        }
        detail_json = requests.post(url=url, data=data1, headers=headers).json()
        json.dump(detail_json, fp=fp, ensure_ascii=False)

print('爬取企业信息完成！')
