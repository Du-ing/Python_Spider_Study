from selenium import webdriver
from time import sleep
from lxml import etree
from base64 import b64decode
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
broser = webdriver.Edge(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver')

broser.get(login_url)
sleep(0.5)
# 点击账号密码登录链接
broser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
sleep(0.5)

# 单独抓取验证码
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
}
page_text = broser.page_source
tree = etree.HTML(page_text)
# 获得base64加密的验证码
img_base64_code = tree.xpath('//*[@id="J-loginImg"]/@src')[0].split('data:image/jpg;base64,')[1]
# 解码获得验证码图片数据
img_data = b64decode(img_base64_code)
with open('./爬虫/6.selenium动态加载数据/code.jpg', 'wb') as fp:
    fp.write(img_data)
    print('验证码下载完毕！')
    fp.close()

# 验证码图片自动识别，获取要点击的坐标
chaojiying = Chaojiying_Client('2385790938', 'whlg201898.', '907586')
im = open('./爬虫/6.selenium动态加载数据/code.jpg', 'rb').read()
site = chaojiying.PostPic(im, 9004)['pic_str']

if '|' in site:
    site_list = site.split('|')
else:
    site_list = []
    site_list.append(site)
print(site_list)

# 模拟输入和点击
broser.find_element_by_id('J-userName').send_keys('xxxxxx')
sleep(0.5)
broser.find_element_by_id('J-password').send_keys('xxxxxx')
sleep(0.5)
img_ele = broser.find_element_by_id('J-loginImg')
for s in site_list:
    x = int(s.split(',')[0])
    y = int(s.split(',')[1])
    ActionChains(broser).move_to_element_with_offset(img_ele, x, y).click.perform()
    sleep(0.5)

broser.find_element_by_id('J-login').click()
sleep(60)
