from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

broser = webdriver.Chrome(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver', chrome_options=chrome_options, options=option)

# 无可视化界面
broser.get('https://www.baidu.com')
sleep(2)
print(broser.page_source)
