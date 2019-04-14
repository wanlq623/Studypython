import requests

#定义爬取有道翻译的函数
def get_youdao(i):
    #翻译url
    url = 'http://fanyi.youdao.com/translate?'
    #模拟请求头文件
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #请求参数
    form_data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15552311507038',
        'sign': 'c87a7b66c3bb7395a9d0c7169ee47317',
        'ts': '1555231150703',
        'bv': 'd1dc01b5ffc1e7dfd53e6ee3c347fc81',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    #post请求
    youdao_res = requests.post(url,headers=headers,data=form_data)
    #打印返回状态
    print('返回状态：%s' % youdao_res.status_code)
    #返回值json处理
    youdao = youdao_res.json()
    #打印翻译结果
    print(youdao['translateResult'][0][0]['tgt'])

#调用函数
if __name__ == '__main__':
    i = input('请输入要翻译的词语：')
    get_youdao(i)