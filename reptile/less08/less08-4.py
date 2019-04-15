import requests,json

#定义获取爬虫数据的函数
def get_web():
    #定义变量input_content输入项
    input_content = input('请输入要联想的词语或者语句：')
    #爬取的url
    url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
    #模拟请求头文件
    headers = {
        'Host': 'ictclas.nlpir.org',
        'Origin': 'http: // ictclas.nlpir.org',
        'Referer': 'http: // ictclas.nlpir.org / nlpir /',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #请求参数
    data = {
        'content': input_content
    }
    #post请求
    web_res = requests.post(url,headers=headers,data=data)
    #打印返回状态
    print('爬虫返回状态：%s' % web_res.status_code)
    #json解析返回数据
    web_json = web_res.json()
    #获w2vlist数据，即联想关键词
    w2vlist = web_json['w2vlist']
    #遍历w2vlist
    for w2 in w2vlist:
        print(w2)

#调动函数
if __name__ == '__main__':
    get_web()