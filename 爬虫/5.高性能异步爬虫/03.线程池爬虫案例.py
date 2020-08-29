import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
# 需求：爬取梨视频的视频数据
# 原则：线程池处理的是阻塞且耗时的操作

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
# 对下述url发起请求解析出品评详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_8'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

dics = []   # 存储所有视频的名字和链接
for li in li_list:
    video_name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'    # 视频名称
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]  # 视频详情页
    # 对视频的url发起请求
    video_page_text = requests.get(url=detail_url, headers=headers).text
    # 从详情页中解析出视频的地址
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, video_page_text)[0]
    video_dic = {
        'name': video_name,
        'url': video_url
    }
    dics.append(video_dic)


def get_video_data(dic):
    url = dic['url']
    print(dic['name']+'正在下载...')
    video_data = requests.get(url=url, headers=headers).content
    # 持久化存储操作
    with open('./爬虫/5.高性能异步爬虫/梨视频爬取/'+dic['name'], 'wb') as fp:
        fp.write(video_data)
        print(dic['name']+'下载成功！')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(len(dics))
pool.map(get_video_data, dics)

pool.close()
pool.join()
