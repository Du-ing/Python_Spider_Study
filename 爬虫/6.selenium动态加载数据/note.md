# selenium模块的基本使用

* 问题：selenium模块和爬虫之间具有怎样的关联？
    * 便捷的获取网站中动态加载的数据
    * 便捷实现模拟登录

* 什么是selenium模块？
    * 基于浏览器自动化的一个模块

* selenium使用流程：
    1. 环境安装：pip install selenium
    2. 下载一个浏览器驱动程序：注意浏览器类型和版本
    3. 实例化一个浏览器对象
    4. 编写基于浏览器自动化的操作代码
        * 发起请求：get(url)
        * 标签定位：find系列的方法
        * 标签交互：send_keys('xxx)、click()
        * 执行JS程序：excute_script('jsCode)
        * 前进、后退：forward()、back()
        * 关闭浏览器：close() 关闭当前窗口、quit() 退出此驱动程序，关闭所有窗口
    5. selenium处理iframe：
        * 如果定位的标签存在于iframe标签之中，则必须使用switch_to.frame(id)进行frame的转换
        * 动作链（拖动）：from selenium import ActionChains
            * 实例化一个动作链对象：action = ActionChains(broser)
            * action.click_and_hold(div)：长按且点击操作
            * action.move_by_offset(x, y)：移动偏量
            * action.perform()：让动作链立即执行
            * action.release()：释放动作链
    
* 12306模拟登陆
    * 超级鹰来识别验证码
    * 12306模拟登陆编码流程：
        1. 使用selenium打开登录页面
        2. 对当前登录页面验证码进行单独提取
        3. 使用超级鹰识别验证码图片（坐标数据）
        4. 使用selenium自动填入信息和点击验证码中的坐标点并登录