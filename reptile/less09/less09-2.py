from selenium import webdriver
import time
from bs4 import BeautifulSoup

#设置Chrome为默认浏览器
dirver = webdriver.Chrome()
#打开网页
dirver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
#2s加载时间
time.sleep(2)
#定义teacher变量赋值为id为teacher
teacher = dirver.find_element_by_id('teacher')
#设定值
teacher.send_keys('吴枫')
#定义assistant变量赋值为id为assistant
assistant = dirver.find_element_by_id('assistant')
#设定值
assistant.send_keys('酱酱')
#定义button变量赋值为属性为button
button = dirver.find_element_by_class_name('sub')
#点击事件
button.click()
#2s加载时间
time.sleep(2)
web_list = dirver.find_elements_by_class_name('content')
for web in web_list:
    title = web.find_element_by_tag_name('h1').text
    comment = web.find_element_by_tag_name('p').text
    print(title, '\n', comment)
# #获取Elements中渲染完成的网页源代码
# pageSource = dirver.page_source
# #使用bs解析
# web_res = BeautifulSoup(pageSource,'html.parser')
# #匹配标签div，属性content的数据
# web_list = web_res.find_all('div',class_='content')
# #遍历web_list
# for web in web_list:
#     #匹配标签h1获取数据
#     title = web.find('h1').text
#     #匹配标签p获取数据
#     comment = web.find('p').text
#     #打印
#     print(title,'\n',comment)
#关闭浏览器
dirver.close()