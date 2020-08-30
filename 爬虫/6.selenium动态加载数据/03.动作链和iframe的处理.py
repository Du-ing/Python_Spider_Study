from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

broser = webdriver.Edge(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver')

broser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签之中的则必须通过如下操作再进行标签定位
broser.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域
div = broser.find_element_by_id('draggable')

# 动作链
action = ActionChains(broser)

for i in range(5):
    # 点击长按指定的标签
    action.click_and_hold(div)
    # perform()立即执行动作链操作
    action.move_by_offset(17, 0).perform()
    sleep(1)
    # 释放动作链
    action.release()

print(div)
