from selenium import webdriver
import time
from bs4 import BeautifulSoup

#设置Chrome为默认浏览器
dirver = webdriver.Chrome()
#打开网页
dirver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
#2s加载时间
time.sleep(2)
#定义username变量赋值为id为user_login
username = dirver.find_element_by_id('user_login')
#设定username输入值
username.send_keys('spiderman')
#定义password变量赋值为id为user_pass
password = dirver.find_element_by_id('user_pass')
#设定password输入值
password.send_keys('crawler334566')
#定义button变量赋值为id为wp-submit
button = dirver.find_element_by_id('wp-submit')
#执行button的click动作
button.click()
#2s加载时间
time.sleep(2)
#跳转页面后找到需要的web_url
# web_url = dirver.find_element_by_id('post-20').find_element_by_tag_name('a').get_attribute('href')
web_url = dirver.find_element_by_link_text('未来已来（三）——同九义何汝秀').get_attribute('href')
# print(web_url)
# pageSource = dirver.page_source
# web_res = BeautifulSoup(pageSource,'html.parser')
# web_list = web_res.find_all('h2',class_ = 'entry-title')[1]
# web_url = web_list.find('a')['href']
#打开新的网页
dirver.get(web_url)
#2s加载
time.sleep(2)
#定义comment变量赋值id为comment
comment = dirver.find_element_by_id('comment')
#设定comment的值
comment.send_keys('selenium操作的留言0415')
#定义sub_button变量id为submit
sub_button = dirver.find_element_by_id('submit')
#执行sub_button的click动作
sub_button.click()
#2s加载时间
time.sleep(2)
#关闭浏览器
dirver.close()
