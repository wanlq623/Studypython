import requests
import csv

#定义爬虫获取网页的函数
def get_web(offset):
    #请求url
    web_url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
    #模拟请求头部文件
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #链接后面的请求参数
    web_params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': offset,
        'limit': '20',
        'sort_by': 'created'
    }
    #发起请求，将响应结果赋值给变量web_res
    web_res = requests.get(web_url , params= web_params , headers = headers)
    #打印返回状态，200表示成功
    print('请求返回状态为：%s'%web_res.status_code)
    #解析返回数据
    web_json = web_res.json()
    return web_json

#定义解析数据的函数
def get_data(data):
    #匹配data获取数据
    web_lists = data['data']
    #定义一个空列表存储数据
    write_list=[]
    #遍历web_lists
    for web_list in web_lists:
        #获取文章标题
        title = web_list['title']
        #获取文章摘要
        excerpt = web_list['excerpt']
        #获取文章链接
        url = web_list['url']
        #把文章标题、文章摘要、文章链接添加进入列表
        write_list.append([title,excerpt,url])
    #print(write_list)
    return write_list

#调用函数
if __name__ == '__main__':
    # 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
    csv_file = open('zhihu.csv', 'a', newline='', encoding='utf-8')
    # 用csv.writer()函数创建一个writer对象。
    writer = csv.writer(csv_file)
    # 创建一个表头列表
    list1 = ['标题', '链接', '摘要']
    #写入表头数据
    writer.writerow(list1)
    #定义offset为0
    offset = 0
    #爬取数量小于100条数据（实际文章数量大于100条）
    while True:
        #页码，根据爬取到的规则每页+20
        offset = offset + 20
        #调用get_web()函数并赋值给变量data
        data = get_web(offset)
        #调用get_data()函数
        get_data(data)
        #遍历get_data()函数返回的列表writer_list的长度
        for i in range(len(get_data(data))):
            #变量datalist赋值
            datalist = get_data(data)[i]
            #写入数据
            writer.writerow(datalist)
        #大于100停止爬取
        if offset > 100:
            break
        #实际文章可根据is_end为true来计算最后一页
        # is_end = data['paging']['is_end']
        # if is_end == False:
        #     for i in range(len(get_data(data))):
        #         datalist = get_data(data)[i]
        #         writer.writerow(datalist)
        # else:
        #     break