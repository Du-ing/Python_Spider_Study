from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

broser = webdriver.Edge(executable_path='./爬虫/6.selenium动态加载数据/msedgedriver')

broser.get('https://qzone.qq.com/')

# 转换到iframe
broser.switch_to_frame('login_frame')
sleep(0.5)

# 定位到账号密码登录选项并点击
choose = broser.find_element_by_id('switcher_plogin')
choose.click()
sleep(1)

# 定位到输入框并填入账号信息
username_input = broser.find_element_by_id('u')
username_input.send_keys('xxxxxxx')
sleep(0.5)
pwd_input = broser.find_element_by_id('p')
pwd_input.send_keys('xxxxxxx')
sleep(0.5)

# 定位到登录按钮并点击
login_button = broser.find_element_by_id('login_button')
login_button.click()
sleep(1)

# 切换到安全验证的iframe
broser.switch_to_frame('tcaptcha_iframe')
# 定位到拖动的标签
drag_tag = broser.find_element_by_id('tcaptcha_drag_thumb')
# 用动作链拖动图片
action = ActionChains(broser)
for end in range(150, 221, 5):
    action.click_and_hold(drag_tag)
    action.move_by_offset(end, 0).perform()
    action.release()
    sleep(0.5)
