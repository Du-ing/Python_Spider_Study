# 将验证码图片下载到本地
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


url = 'https://so.gushiwen.org/user/login.aspx'
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

code_img_src = 'https://so.gushiwen.org' + tree.xpath(
    '//img[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src, headers=headers).content

with open('./爬虫/3.验证码/code.jpg', 'wb') as fp:
    fp.write(img_data)
print('验证码加载完毕！')

code = testFunc('./爬虫/3.验证码/code.jpg', '30400')
print(code)
