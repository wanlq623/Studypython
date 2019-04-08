import requests
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

commentid = ''
for i in range(5):
    params = {
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '102065756',
        'cmd': '8',
        'needcommentcrit': '0',
        'pagenum': str(x),
        'pagesize': '25',
        'lasthotcommentid': commentid,
        'domain': 'qq.com',
        'ct': '24',
        'cv': '101010  '
    }
    res_comment = requests.get(url,params=params)

    json_comment = res_comment.json()
    list_comment = json_comment['comment']['commentlist']
    for comment in list_comment:
        print(comment['rootcommentcontent'])
    commentid = list_comment[24]['commentid']




# import requests
# # 引用requests库
# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # 调用get方法，下载这个字典
# json_music = res_music.json()
# # 使用json()方法，将response对象，转为列表/字典
#
# song_lists = json_music['data']['song']['list']
# #一层一层地取字典，获取歌单列表
#
# for song_list in song_lists:
#     song_name = song_list['name']
#     song_zhuanji = song_list['album']['name']
#     song_time = song_list['interval']
#     song_url = song_list['url']
#     print('歌名：%s\n专辑：%s\n播放时长：%s秒\n链接：%s'%(song_name,song_zhuanji,song_time,song_url))