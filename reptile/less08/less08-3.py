import requests,json

#定义机器人函数
def get_turing():
    #接口地址
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    #定义变量为输入项
    text_input = input('我：')
    #请求参数
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text_input
            },
            "selfInfo": {
                "location": {
                    "city": "广州",
                    "province": "天河区",
                    "street": "棠下村"
                }
            }
        },
        "userInfo": {
            "apiKey": "输入自己的apikey",
            "userId": "OnlyUseAlphabet"
        }
    }
    #将请求参数json格式化
    data = json.dumps(data)
    #post请求
    res = requests.post(url,data=data)
    #json数据格式化
    res_json = res.json()
    #解析返回结果的text文本
    mesage = res_json['results'][0]['values']['text']
    print(mesage)

#调用函数
if __name__ == '__main__':
    get_turing()
