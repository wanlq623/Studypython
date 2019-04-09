import requests
import re

#定义获取搜索歌曲的函数
def get_music(w,p):
    # 搜索音乐的url
    music_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
    # 模拟请求头文件，搜索歌曲部分
    music_headers = {
        # 请求来源
        'origin': 'https://y.qq.com',
        # 请求来源，携带的信息比“origin”更丰富
        'referer': 'https://y.qq.com/portal/search.html',
        # 标记了请求从什么设备，什么浏览器上发出
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    # music_url链接后面请求的参数
    music_params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '49611450758870577',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': p,
        'n': '10',
        'w': w,
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
    # 返回一个response对象，赋值给res_music
    res_music = requests.get(music_url, params=music_params, headers=music_headers)
    # 打印返回状态
    print('请求获取歌曲返回状态：' + str(res_music.status_code))
    print('-------------返回状态分割线---------------')
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music.json()
    # 匹配data-song-list获取元素
    song_lists = json_music['data']['song']['list']
    song_ids = []
    # 遍历song_lists
    for song_list in song_lists:
        # 匹配id获取歌曲id
        song_id = song_list['id']
        song_ids.append(song_id)
    return song_ids

#定义获取歌词的函数
def get_lyric(song_id):
    # 获取歌词的url
    lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    # 模拟请求头,歌词部分
    lyric_headers = {
        # 请求来源
        'origin': 'https://y.qq.com',
        # 请求来源
        'referer': 'https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html',
        # 标记了请求从什么设备，什么浏览器上发出
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    # lyric_url链接后面请求的参数
    lyric_params = {
        'nobase64': '1',
        'musicid': song_id,
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
    # 返回一个response对象，赋值给res_lyric
    res_lyric = requests.get(lyric_url, params=lyric_params, headers=lyric_headers)
    # 打印返回状态
    print('请求获取歌词返回状态：' + str(res_lyric.status_code))
    print('-------------返回状态分割线---------------')
    # 使用json()方法，将response对象，转为列表/字典
    json_lyric = res_lyric.json()
    #匹配lyric获取歌词数据
    song_lyric = json_lyric['lyric']
    # 格式化歌词
    dr1 = re.compile(r'&#\d.;', re.S)
    dr2 = re.compile(r'\[\d+\]', re.S)
    lyrics = dr1.sub(r'', song_lyric)
    lyrics = dr2.sub(r'\n', lyrics).replace('\n\n', '\n')
    #返回歌词
    return lyrics

#调用函数，获取歌词
w = input('请输入要搜索的歌手姓名：')
for i in range(5):
    #定义页面
    p = i + 1
    songs = get_music(w,p)
    for x in range(len(songs)):
        song_id = songs[x]
        print(get_lyric(song_id))
        print('-------------可爱的分割线---------------')
        print('')








#普通写法
# #搜索音乐的url
# music_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
#
# #获取歌词的url
# lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
#
# #请求搜索结果后前5页的歌曲
# for i in range(5):
#
#     # 模拟请求头文件，搜索歌曲部分
#     music_headers = {
#         # 请求来源
#         'origin': 'https://y.qq.com',
#         # 请求来源，携带的信息比“origin”更丰富
#         'referer': 'https://y.qq.com/portal/search.html',
#         # 标记了请求从什么设备，什么浏览器上发出
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     }
#
#     #定义页码
#     p = i+1
#
#     #music_url链接后面请求的参数
#     music_params = {
#         'ct': '24',
#         'qqmusic_ver': '1298',
#         'new_json': '1',
#         'remoteplace': 'txt.yqq.song',
#         'searchid': '49611450758870577',
#         't': '0',
#         'aggr': '1',
#         'cr': '1',
#         'catZhida': '1',
#         'lossless': '0',
#         'flag_qc': '0',
#         'p': str(p),
#         'n': '10',
#         'w': '周杰伦',
#         'g_tk': '5381',
#         'loginUin': '0',
#         'hostUin': '0',
#         'format': 'json',
#         'inCharset': 'utf8',
#         'outCharset': 'utf-8',
#         'notice': '0',
#         'platform': 'yqq.json',
#         'needNewCode': '0'
#     }
#     #返回一个response对象，赋值给res_music
#     res_music = requests.get(music_url , params = music_params,headers = music_headers)
#
#     #打印返回状态
#     print('请求获取歌曲返回状态：' + str(res_music.status_code))
#
#     #使用json()方法，将response对象，转为列表/字典
#     json_music = res_music.json()
#
#     #匹配data-song-list获取元素
#     song_lists = json_music['data']['song']['list']
#
#     #遍历song_lists
#     for song_list in song_lists:
#
#         #匹配name获取歌名数据
#         song_name = song_list['name']
#
#         #匹配album-name获取专辑名称
#         song_album = song_list['album']['name']
#
#         #匹配id获取歌曲id
#         song_id = song_list['id']
#
#         #模拟请求头,歌词部分
#         lyric_headers = {
#             # 请求来源
#             'origin':'https://y.qq.com',
#             # 请求来源
#             'referer':'https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html',
#             # 标记了请求从什么设备，什么浏览器上发出
#             'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#             }
#
#         # lyric_url链接后面请求的参数
#         lyric_params = {
#             'nobase64': '1',
#             'musicid': song_id,
#             '-': 'jsonp1',
#             'g_tk': '5381',
#             'loginUin': '0',
#             'hostUin': '0',
#             'format': 'json',
#             'inCharset': 'utf8',
#             'outCharset': 'utf-8',
#             'notice': '0',
#             'platform': 'yqq.json',
#             'needNewCode': '0'
#         }
#
#         #返回一个response对象，赋值给res_lyric
#         res_lyric = requests.get(lyric_url , params = lyric_params , headers = lyric_headers)
#
#         #打印返回状态
#         print('请求获取歌词返回状态：' + str(res_lyric.status_code))
#
#         #使用json()方法，将response对象，转为列表/字典
#         json_lyric = res_lyric.json()
#
#         #print(json_lyric)
#         song_lyric = json_lyric['lyric']
#         #print(type(song_lyric))
#         #格式化歌词
#         dr1 = re.compile(r'&#\d.;', re.S)
#         dr2 = re.compile(r'\[\d+\]', re.S)
#         lyrics = dr1.sub(r'', song_lyric)
#         lyrics = dr2.sub(r'\n', lyrics).replace('\n\n', '\n')
#         print(lyrics)
#         print('')
#         print('--------------------------------')
#         print('')
#
#
#
