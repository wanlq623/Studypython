import requests,smtplib,time,schedule
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

#定义爬取天气网的函数
def get_weather():
    #爬取的目标网址url
    url = 'http://www.weather.com.cn/weather/101280101.shtml'
    #模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #请求地址并返回response赋值给res
    res = requests.get(url,headers=headers)
    #采用utf-8的编码格式
    res.encoding = 'utf-8'
    #打印返回状态
    print('返回状态：%s' % res.status_code)
    #使用BeautifulSoup解析
    soup = BeautifulSoup(res.text,'html.parser')
    #获取7天的天气
    weathers = soup.find('ul',class_ = 't clearfix').find_all('li')
    #遍历weathers
    for weather in weathers:
        #获取天气日期
        date = weather.find('h1').text
        #获取天气预报
        wea = weather.find(class_ = 'wea').text
        #获取温度
        tem = weather.find(class_ = 'tem').text.strip()
        #打印结果
        weather_day = '日期：%s天气：%s温度：%s' %(date,wea,tem)
        return weather_day

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
    subject_mail = '天气预报自动推送'
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
    weather_day = get_weather()
    get_email(weather_day)
    print('任务结束')

#调用函数
if __name__ == '__main__':
    # 设定定时任务
    schedule.every().day.at('15:30').do(get_sendmail)
    while True:
        schedule.run_pending()
        time.sleep(1)