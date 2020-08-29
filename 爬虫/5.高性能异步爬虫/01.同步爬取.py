import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}

urls = [
    'http://downsc.chinaz.net/Files/download/png4/202008/7828.rar',
    'http://downsc.chinaz.net/Files/download/icon4/202008/7819.rar',
    'http://downsc.chinaz.net/Files/download/icon4/202008/7817.rar'
]


def get_content(url):
    # get方法其实是一个阻塞的方法
    print('正在爬取：', url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print('响应数据的长度为：', len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
