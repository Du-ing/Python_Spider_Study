from chaojiying import Chaojiying_Client

chaojiying = Chaojiying_Client('2385790938', 'whlg201898.', '907586')   # 用户中心>>软件ID 生成一个替换 96001
im = open('./爬虫/6.selenium动态加载数据/test.jpg', 'rb').read()     # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
site = chaojiying.PostPic(im, 9004)['pic_str']
print('点击的坐标有：', site)
print(type(site))
