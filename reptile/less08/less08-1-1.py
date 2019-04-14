import requests
session = requests.session()

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
tel = input('请输入手机号码：')
data_1 = {'captcha_hash':'',
        'captcha_value':'',
        'mobile':tel,
        'scf':''}
token = session.post(url_1, headers=headers, data=data_1).json()['validate_token']
url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
code = input('请输入手机验证码：')
data_2 = {'mobile':tel,
        'scf':'ms',
        'validate_code':code,
        'validate_token':token}
session.post(url_2,headers=headers,data=data_2)
address_url = 'https://www.ele.me/restapi/v2/pois?'
place = input('请输入你的收货地址：')
params = {'extras[]':'count','geohash':'wtw3sjq6n6um','keyword':place,'limit':'20','type':'nearby'}
#这里使用了广州的geohash
address_res = requests.get(address_url,params=params)
address_json = address_res.json()
print('以下，是与'+place+'相关的位置信息：\n')
n=0
for address in address_json:
    print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    n = n+1
address_num = int(input('请输入您选择位置的序号：'))
final_address = address_json[address_num]
restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants?'
#使用带有餐馆列表的那个XHR地址。
params = {
    'extras[]':'activities',
    'geohash':final_address['geohash'],
    'latitude':final_address['latitude'],
    'limit':'24',
    'longitude':final_address['longitude'],
    'offset':'0',
    'terminal':'web'
}
#将参数封装，其中geohash和经纬度，来自前面获取到的数据。
restaurants_res = session.get(restaurants_url,params=params)
#发起请求，将响应的结果，赋值给restaurants_res
restaurants = restaurants_res.json()
#把response对象，转为json。
for restaurant in restaurants:
#restsurants最外层是一个列表，它可被遍历。restaurant则是字典，里面包含了单个餐厅的所有信息。
    print(restaurant['name'])
# </code></pre><h1>一份总结：</h1>
# <p>就是这样一个代码，它能拿到给定位置附近的餐厅名。但它的潜力并不只是如此。  </p>
# <p>如果我们尝试加载饿了么官网的首页，能够找到一个xhr叫做cities，这个xhr里包含了全国两千多个城市的经纬度。  </p>
# <p>利用Python的geohash模块，你可以将经纬度数据，转化为geohash（当然，也可以将geohash转为经纬度，我也是用这种方式，发现我的默认geohash是深圳）。  </p>
# <p>那么在理论上，其实你可以通过这种方式，拿到全国餐厅的数据……  </p>
# <p>只要稍做扩展，它还能拿到许多数据：所有的餐厅名/电话号码/评分/品牌/经纬度/介绍/均价/月销量……  </p>
# <p>此时，这个爬虫就具备了商业价值，它能胜任许多数据分析的工作：选址策略、定价策略、差异化竞争、2B营销……  </p>
# <p><img src="https://res.pandateacher.com/practice08-5-2019125.png" alt="practice08-5-2019125">  </p>
# <p>或许你会质疑自己能不能做到像我描述的这样厉害，不用怕，很快你就能够做到对此心中有数。  </p>
# <p>而在后续的关卡，当你学会反爬虫的应对策略、协程、Scrapy框架……你会变得像我说的那样强大。  </p>
# <p>再会！</p>