from selenium import webdriver
from time import sleep

broser = webdriver.Edge(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver')

broser.get('https://www.taobao.com/')

# 定位到输入框
search_input = broser.find_element_by_id('q')
# 输入框交互
search_input.send_keys('电脑')
sleep(2)

# 执行一组JS程序，实现滚轮操作
broser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 定位到搜索按钮并点击
submit = broser.find_element_by_class_name('btn-search')
submit.click()
sleep(2)

broser.get('https://www.baidu.com')
sleep(2)
# 回退
broser.back()
sleep(2)
broser.forward()

sleep(5)
broser.quit()
