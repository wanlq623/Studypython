import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from_addr = input('请输入邮件用户名，格式：xxx@qq.com')
password = input('请输入密码')

to_addrs = input('请输入收件人邮箱地址')

smtp_server = 'smtp.qq.com'

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header(from_addr)
msgRoot['To'] = Header(",".join(to_addrs))
msgRoot['Subject'] = Header('这是Python机器人自动发送的测试邮件')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)



mail_msg = '''
<p>这是Python机器人自动发送的邮件测试信息！！！！</P>
<p><img src="cid:image1"></p>
'''
#指定图片为当前目录
fp = open('test.png','rb')
msgImage = MIMEImage(fp.read())
fp.close()

#定义图片ID，在html文本中引用
msgImage.add_header('Content-ID','<image1>')
msgRoot.attach(msgImage)

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr,password)
server.sendmail(from_addr,to_addrs,msgRoot.as_string())
server.close()