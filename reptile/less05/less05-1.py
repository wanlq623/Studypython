import requests
url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

params = {
    'nobase64': '1',
    'musicid': '102065756',
    '-': 'jsonp1',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
}
res_comment = requests.get(url,params=params)
print('返回状态：' + str(res_comment.status_code))
json_comment = res_comment.json()
print(json_comment)