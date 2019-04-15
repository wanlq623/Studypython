from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 实例化Option对象
chrome_options = Options()
# 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')
# 设置引擎为Chrome，在后台默默运行
driver = webdriver.Chrome(options = chrome_options)
# 打开网页
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
#等待2s
time.sleep(2)
button = driver.find_element_by_class_name('js_get_more_hot')
button.click()
time.sleep(2)
#匹配js_hot_list和js_cmt_li获取评论数据
comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
#print(len(comments))
#遍历comments
for comment in comments:
    #匹配p标签获取评论数据
    sweet = comment.find_element_by_tag_name('p')
    #打印
    print('评论：%s\n' % sweet.text)
#关闭浏览器
driver.close()