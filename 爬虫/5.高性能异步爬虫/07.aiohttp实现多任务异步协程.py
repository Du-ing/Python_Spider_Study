import aiohttp
import asyncio
import time

urls = {
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
}


async def get_page(url):
    print('正在下载：', url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回json对象
            # 注意：获取响应数据之前一定要使用await进行手动挂起
            page_text = await response.text()
    print('下载数据为：', page_text)


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
