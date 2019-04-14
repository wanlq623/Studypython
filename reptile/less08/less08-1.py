import requests,json

#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies
session = requests.session()
#模拟请求头文件
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

#定义获取cookies的函数
def get_cookies(token):
    #定义变量validate_code手机验证码为输入项
    validate_code = input('请输入短信验证码：')
    #登录url
    url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    #请求参数，变量为mobile、validate_code、token
    data = {
        'mobile': mobile,
        'scf': "ms",
        'validate_code': validate_code,
        'validate_token': token
    }
    # 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参
    web_res = session.post(url,headers=headers,data=data)
    return (web_res)

#定义获取短信验证码的函数
def mobile_code():
    #发送验证码的url
    url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
    #请求参数，变量为mobile
    data = {
        'captcha_hash': "",
        'captcha_value': "",
        'mobile': mobile,
        'scf': "ms"
    }
    #采用post方式请求
    mobile_send_code = requests.post(url,headers=headers,data=data)
    #返回请求结果
    print('短信验证码返回结果：%s' % mobile_send_code.status_code)
    #获取token
    token = mobile_send_code.json()['validate_token']
    return (token)

#定义获取商家列表的函数
def shop_list():
    #地址搜索url
    address_url = 'https://www.ele.me/restapi/v2/pois?'
    #定义变量place为输入项
    address = input('请输入你的收货地址：')
    #请求参数，变量为place
    params = {
        'extras[]': 'count',
        'geohash': 'wtw3sjq6n6um',
        'keyword': address,
        'limit': '20',
        'type': 'nearby'
    }
    #采用request.get方式请求并返回数据复制给address_res
    address_res = requests.get(address_url, params=params,headers=headers)
    #数据json格式化处理
    address_json = address_res.json()
    #打印位置信息
    print('以下，是与' + address + '相关的位置信息：\n')
    n = 0
    for address_list in address_json:
        print(str(n) + '. ' + address_list['name'] + '：' + address_list['short_address'] + '\n')
        n = n + 1
    address_num = int(input('请输入您选择位置的序号：'))
    final_address = address_json[address_num]
    #商家列表url
    url = 'https://www.ele.me/restapi/shopping/restaurants?'
    #请求参数
    parmas = {
        'extras[]': 'activities',
        'geohash': final_address['geohash'],
        'latitude': final_address['latitude'],
        'limit': '24',
        'longitude': final_address['longitude'],
        'offset': '0',
        'terminal': 'web'
    }
    #采用get方式请求
    shop_listres = session.get(url,headers=headers,params=parmas)
    #打印返回状态
    print('商家列表返回状态：%s' % shop_listres.status_code)
    #采用json解析数据
    shop_json = shop_listres.json()
    #遍历shop_json
    for shop_list in shop_json:
        shop_name = shop_list['name']
        shop_address = shop_list['address']
        print('商家名称：%s\n商家地址：%s\n' % (shop_name,shop_address))

#调用函数
if __name__ == '__main__':
    mobile = input('请输入登录手机号码')
    token = mobile_code()
    get_cookies(token)
    shop_list()






