import requests
import asyncio
import time

urls = {
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
}


async def get_page(url):
    print('正在下载：', url)
    # requests模块发起的请求是基于同步的，必须使用基于异步的网络请求模块
    response = requests.get(url=url)
    print('下载数据为：', response.text)


tasks = []

start = time.time()
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时：', end-start)
