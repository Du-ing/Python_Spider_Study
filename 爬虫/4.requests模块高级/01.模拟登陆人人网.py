# 模拟登陆流程
# 1. 验证码的识别，获取验证码图片的文字数据
# 2. 将验证数据加入到登录的post请求参数中
# 3. 对post请求进行发送（处理请求参数）
# 4. 对响应数据进行分析和持久化存储

import requests
from lxml import etree
from api import FateadmApi


# 执行验证的方法
def testFunc(filePath, type):
    pd_id = "125665"  # 用户中心页可以查询到pd信息
    pd_key = "hfUQ60EpYSsLTLJkU5673zky/zExwhTA"
    app_id = "325665"  # 开发者分成用的账号，在开发者中心可以查询到
    app_key = "D6oiPFGNhz3662mfIWZNVCi1/gTe4Etl"
    # 识别类型，
    # 具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
    pred_type = type
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    # 查询余额
    balance = api.QueryBalcExtend()  # 直接返余额
    print('所剩余额：'+str(balance))
    # api.QueryBalc()

    # 通过文件形式识别：
    file_name = filePath
    # 多网站类型时，需要增加src_url参数，具体请参考api文档: http://docs.fateadm.com/web/#/1?page_id=6
    result = api.PredictFromFileExtend(pred_type, file_name)   # 直接返回识别结果
    rsp = api.PredictFromFile(pred_type, file_name)  # 返回详细识别结果
    '''
    # 如果不是通过文件识别，则调用Predict接口：
    # result 			= api.PredictExtend(pred_type,data)   	# 直接返回识别结果
    rsp             = api.Predict(pred_type,data)				# 返回详细的识别结果
    '''

    just_flag = False
    if just_flag:
        if rsp.ret_code == 0:
            # 识别的结果如果与预期不符，可以调用这个接口将预期不符的订单退款
            # 退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
            api.Justice(rsp.request_id)

    # card_id         = "123"
    # card_key        = "123"
    # 充值
    # api.Charge(card_id, card_key)
    # LOG("print in testfunc")

    return result


# 捕获验证码图片
url = 'http://www.renren.com/SysHome.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(code_img_src, headers=headers).content
with open('./爬虫/4.requests模块高级/code.jpg', 'wb') as fp:
    fp.write(code_img_data)
    print('验证码加载完毕！')

# 验证码图片识别
code = testFunc('./爬虫/4.requests模块高级/code.jpg', '30600')
# print(code)

# post请求的发送（模拟登录）
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202075143549'
data = {
    'email': '2385790938@qq.com',
    'icode': code,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '41e3d06f77c5c4654f4575c5466e091658e7cb30bb3c6d868aa75efa763e9946',
    'rkey': '4c43d688ad0e525536dd626bf9a4cf7b',
    'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DM5jR4aNe2K00lUdfWMqs6RBSyTGgSXDFhOMhuPG6C4u%26wd%3D%26eqid%3Dd382eba10001fdf7000000055f48a73d'
}
response = requests.post(url=login_url, heaaders=headers, data=data)
if(response.status_code == 200):
    login_page_text = response.text
    with open('./爬虫/4.requests模块高级/人人网.html', 'w', encoding='utf-8') as fp:
        fp.write(login_page_text)
