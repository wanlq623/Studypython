import requests,json

#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies
session = requests.session()
#模拟请求头文件
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

#定义读取cookies函数
def read_cookies():
    # 以reader读取模式，打开名为cookies.txt的文件
    cookies = open('cookies.text', 'r')
    # 调用json模块的loads函数，把字符串转成字典
    rcookies_dict = json.load(cookies)
    # 把转成字典的cookies再转成cookies本来的格式
    cookies = requests.utils.cookiejar_from_dict(rcookies_dict)
    # 获取cookies：就是调用requests对象（session）的cookies属性
    return (cookies)

#定义存储cookies函数
def save_cookies():
    # 登录URL
    login_url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    #请求参数
    form_data = {
        'log': input('请输入登录账号'),
        'pwd': input('请输入密码'),
        'rememberme': 'forever',
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
        'testcookie': '1'
    }
    #在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参
    session.post(login_url,headers=headers,data=form_data)
    #把cookies转化成字典
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #调用json模块的dumps函数，把cookies从字典再转成字符串
    cookies_str = json.dumps(cookies_dict)
    #将cookies存入文本文件
    with open('cookies.text','w') as cookies_file:
        cookies_file.write(cookies_str)

#定义写评论的函数
def writer_comment():
    #发表评论的url
    comment_url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
    #请求参数
    comment_data = {
        'comment': input('请输入评论：'),
        'submit': '发表评论',
        'comment_post_ID': '23',
        'comment_parent': '0'
    }
    #在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment
    comment_res = session.post(comment_url,headers=headers,data=comment_data)
    return (comment_res)

#调用函数
if __name__ == '__main__':
    #如果能读取到cookies文件，执行以下代码，跳过except的代码
    try:
        session.cookies = read_cookies()
    #如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies
    except FileNotFoundError:
        save_cookies()
        session.cookies = read_cookies()

    #定义变量num，赋值writer_commnent()函数返回值，通过if判断状态是为200，如果不是重新登录（账号：spiderman;密码：crawler334566）
    num = writer_comment()
    if num.status_code == 200:
        print('发表评论成功。')
    else:
        save_cookies()
        session.cookies = read_cookies()
        num = writer_comment()







#面向过程写法
# #用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies
# session = requests.session()
# #模拟请求头文件
# login_headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# #如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论
# try:
#     # 以reader读取模式，打开名为cookies.txt的文件
#     cookies_text = open('cookies.text', 'r')
#     # 调用json模块的loads函数，把字符串转成字典
#     rcookies_dict = json.load(cookies_text)
#     # 把转成字典的cookies再转成cookies本来的格式
#     cookies_r = requests.utils.cookiejar_from_dict(rcookies_dict)
#     # 获取cookies：就是调用requests对象（session）的cookies属性
#     session.cookies = cookies_r
# #如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论
# except FileNotFoundError:
#     #登录URL
#     login_url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
#
#     #请求参数
#     form_data = {
#         'log': input('请输入登录账号'),
#         'pwd': input('请输入密码'),
#         'rememberme': 'forever',
#         'wp-submit': '登录',
#         'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
#         'testcookie': '1'
#     }
#     #post请求，请求结果赋值给变量login_res(使用session之前）
#     # login_res = requests.post(login_url,headers = login_headers,data=form_data)
#     #在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参
#     session.post(login_url,headers = login_headers,data=form_data)
#     #把cookies转化成字典
#     cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#     print(cookies_dict)
#     #调用json模块的dumps函数，把cookies从字典再转成字符串
#     cookies_str = json.dumps(cookies_dict)
#     print(cookies_str)
#     #将cookies存入文本文件
#     with open('cookies.text','w') as cookies_file:
#         cookies_file.write(cookies_str)
#     #提取cookies值
#     # login_cookies = login_res.cookies
#
#
# #发表评论的url
# comment_url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
# #请求参数
# comment_data = {
#     'comment': input('请输入评论：'),
#     'submit': '发表评论',
#     'comment_post_ID': '23',
#     'comment_parent': '0'
# }
# #用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment_res
# # comment_res = requests.post(comment_url,headers=login_headers,data=comment_data,cookies=login_cookies)
# #在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment
# comment_res = session.post(comment_url,headers=login_headers,data=comment_data)
# #打印返回状态
# # print('返回状态：%s' % comment_res.status_code)
