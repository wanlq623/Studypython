import requests,smtplib,time,schedule,json
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

#定义获取菜谱的函数
def get_caipu():
    #爬取目标网站url
    url = 'http://www.xiachufang.com/explore/'
    #模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 返回一个response对象，赋值给res
    res = requests.get(url,headers=headers)
    # 打印请求状态，返回200为请求正常
    print('返回状态：' + str(res.status_code))
    # 把网页解析为BeautifulSoup对象
    soup = BeautifulSoup(res.text, 'html.parser')
    # 通过匹配属性class='info pure-u'，提取出我们想要的元素
    items = soup.find_all(class_='info pure-u')
    #菜谱链接前半段
    web_url = 'http://www.xiachufang.com'
    # 定义一个空的列表存放菜谱
    food_list = []
    # 遍历列表items
    for item in items:
        food_name = item.find('a').text[17:-13]
        food_url = web_url + item.find('a')['href']
        food_value = item.find(class_='ing ellipsis').text[1:-1]
        food_list.append(['&美食名称：%s,美食链接：%s,美食材料：%s'%(food_name, food_url, food_value)])
    #json转字符串
    foods = json.dumps(food_list,ensure_ascii=False)
    return (foods.replace('[','').replace(']','').replace('"','').replace(',','\n').replace('&','\n'))

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
    subject_mail = '机器人推送-本周最受欢迎菜谱'
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
    food_list = get_caipu()
    get_email(food_list)
    print('任务结束')

#调用函数
if __name__ == '__main__':
    # 设定定时任务
    schedule.every().friday.at('08:00').do(get_sendmail)
    while True:
        schedule.run_pending()
        time.sleep(1)
