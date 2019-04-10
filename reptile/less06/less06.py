import openpyxl
import requests

#定义变量w
w = input('请输入你喜欢的歌手姓名：')
#创建工作簿
wb = openpyxl.Workbook()
#获取工作簿的活动表
sheet = wb.active
#工作表明码为song
sheet.title = 'song'
#把'歌曲名','所属专辑','播放时长','播放链接'分别写入到'A1','B1','C1','D1'单元格中
sheet['A1'] = '歌曲名'
sheet['B1'] = '所属专辑'
sheet['C1'] = '播放时长'
sheet['D1'] = '播放链接'

#爬取5页数据
for i in range(5):
    p = i+1
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
    print('-------------返回状态分割线---------------')
    print('请求获取第%s页歌曲返回状态：%s' %(p,res_music.status_code))
    print('-------------返回状态分割线---------------')
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music.json()
    # 匹配data-song-list获取元素
    song_lists = json_music['data']['song']['list']

    # 遍历song_lists
    for song_list in song_lists:
        #匹配name获取歌曲名称
        song_name = song_list['name']
        #匹配album-name获取专辑名称
        song_album = song_list['album']['name']
        #匹配interval获取歌曲播放时长
        song_time = song_list['interval']
        #匹配url获取歌曲链接
        song_url = song_list['url']
        #把数据写入文件
        sheet.append([song_name,song_album,song_time,song_url])
        print('%s  写入成功'%song_name)

#保存文件
wb.save('songs.xlsx')




