from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象（传入浏览器驱动）
broser = webdriver.Edge(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver')

broser.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取浏览器当前页面的源码数据
page_text = broser.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

sleep(5)
broser.quit()
