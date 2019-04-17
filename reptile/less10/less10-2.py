import requests,smtplib,time,schedule,json,random,urllib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

#定义爬虫获取随机电影的函数
def get_web(start):
    #请求url
    url = 'https://movie.douban.com/top250?start=%s&filter=' % start
    #模拟请求头文件
    header = {
        'User - Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #返回一个response对象，赋值给movie_res
    res_movie = requests.get(url,headers = header)
    #打印请求状态，返回200为请求正常
    print('返回状态：' + str(res_movie.status_code))
    #把网页解析为BeautifulSoup对象
    movie_soup = BeautifulSoup(res_movie.text,'html.parser')
    #匹配标签ol获取数据，再匹配标签li获取全部数据
    movies = movie_soup.find('ol').find_all('li')
    # 写入数据列表
    movies_list = []
    # 遍历all_movie
    for movie in movies:
        # 获取电影名称
        name = movie.find('span').text
        #添加到影片列表
        movies_list.append(name)
    #随机选择三部电影
    movies_random = random.sample(movies_list,3)
    return movies_random

#定义获取电影下载链接的函数
def get_dowloadurl(movies_random):
    dowloadurl_list = []
    #遍历movies_random
    for movie_name in movies_random:
        # 定义用户输入的查询电影的变量
        user_name = movie_name.encode('gbk')
        print('爬虫正在工作中，请稍等....')
        # 使用urllib库中的quote函数转换成url的编码
        movie_name = urllib.parse.quote(user_name)
        # 初始url
        url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
        # 拼装输入结果后的地址
        serch_url = url + movie_name
        #通过requests get方式请求数据
        serch_res = requests.get(serch_url)
        #打印返回结果
        print('搜索返回结果：' + str(serch_res.status_code))
        #解析数据
        serch_soup = BeautifulSoup(serch_res.text, 'html.parser')
        #获取搜索电影详细的url
        movie_url = serch_soup.find('div', class_='co_content8').find_all('a')[0]['href']
        #拼装完整的电影详细url
        movie_serchurl = 'http://s.ygdy8.com' + movie_url
        # 根据下载地址返回一个response对象，赋值给movie_res
        movie_res = requests.get(movie_serchurl)
        #返回结果编码
        movie_res.encoding = 'gbk'
        #打印返回结果
        print('详细页面返回结果：' + str(movie_res.status_code))
        #解析数据
        movie_soup = BeautifulSoup(movie_res.text, 'html.parser')
        #获取下载地址
        movie_downurl = movie_soup.find('div', class_='co_content8').find('tbody').find('a')['href']
        dowloadurl_list.append('%s 下载地址是：%s' % (user_name.decode('gbk'), movie_downurl))
    # json转字符串
    movie_down = json.dumps(dowloadurl_list, ensure_ascii=False)
    return (movie_down.replace('[', '').replace(']', '').replace(',', '\n').replace('"',''))

#定义发送邮件的函数
def get_email(weather_day):
    #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    mailhost = 'smtp.qq.com'
    #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail = smtplib.SMTP_SSL(mailhost)
    #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号
    qqmail.connect(mailhost,465)

    #定义发送邮件账号
    username_mail = '输入自己邮箱的账号'
    #定义发送邮件密码或授权码
    password_mail = '输入自己邮箱的授权码'
    #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
    qqmail.login(username_mail,password_mail)

    #收入收件人邮箱地址
    receiver = '输入收件地址'
    #定义变量赋值邮件内容
    content_mail = weather_day
    #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
    message = MIMEText(content_mail,'plain','utf-8')
    #定义邮件主题
    subject_mail = '机器人推送-本周电影推荐'
    #在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']
    message['Subject'] = Header(subject_mail,'utf-8')

    #异常处理
    try:
        qqmail.sendmail(username_mail,receiver,message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

#定义定时发送邮件的函数
def get_sendmail():
    print('开始任务')
    movie_down = get_dowloadurl(get_web(1))
    get_email(movie_down)
    print('任务结束')

if __name__ == '__main__':
    #设定定时任务
    schedule.every().friday.at('08:00').do(get_sendmail)
    while True:
        schedule.run_pending()
        time.sleep(1)
    # movie_down = get_dowloadurl(get_web(1))
    # print(movie_down)
    #get_sendmail()

