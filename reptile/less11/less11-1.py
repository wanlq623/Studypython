from gevent import monkey
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步
monkey.patch_all()
import gevent,time,requests
from bs4 import BeautifulSoup
from gevent.queue import Queue

#定义获取所有爬取网页地址的函数
def get_allurl():
    url_list = []
    for i in range(2,11):
        start_url = 'http://www.mtime.com/top/tv/top100/'
        new_url = start_url + ('index-%s.html'%i)
        url_list.append(start_url)
        url_list.append(new_url)
    return url_list

#创建队列队形，并赋值给work
work = Queue()
#遍历url_list
for url in get_allurl():
    #用put_nowait()函数可以把网址都放进队列里
    work.put_nowait(url)

#定义爬虫函数
def crawler():
    #当队列不是空的时候，就执行下面代码
    while not work.empty():
        #用get_nowait()函数把队列里面的网址取出来
        url = work.get_nowait()
        #requests.get请求url
        tv_res = requests.get(url)
        #打印网址、队列长度、抓取请求的状态码
        print('请求网址：%s\n目前队列长度：%s\n请求网址返回的状态：%s\n----------------------'%(url,work.qsize(),tv_res.status_code))
        #解析数据
        tv_soup = BeautifulSoup(tv_res.text,'html.parser')
        #匹配标签div和属性top_list获取数据
        tvs_list = tv_soup.find('div',class_ = 'top_list')
        #遍历tvs_list
        for tv_list in tvs_list:
            # 获取序号
            em = tv_list.find('div', class_='number').find('em').text
            # 获取电视剧名称
            name = tv_list.find('div', class_='mov_con').find('h2').text
            # 获取导演、主演列表
            mov_con = tv_list.find('div', class_='mov_con').find_all('p')
            try:
                # 获取导演
                director = mov_con[0].text
            # 异常处理
            except IndexError:
                director = ''
            try:
                # 获取主演
                actors = mov_con[1].text.replace('\t\t\xa0',',')
            # 异常处理
            except IndexError:
                actors = ''
            # 获取介绍列表
            introduces = tv_list.find('div', class_='mov_con').find('p', class_='mt3')
            # 判断介绍有值
            if introduces:
                # 获取介绍
                introduce = introduces.text
            else:
                introduce = '此片没有介绍'
            print('序号：%s\n电视剧名称：%s\n%s\n%s\n%s\n------------------' % (em, name, director, actors, introduce))

#创建空的任务列表
tasks_list = []
#相当于创建2个爬虫
for i in range(2):
    #用gevent.spawn()函数创建执行crawler()函数的任务
    task = gevent.spawn(crawler)
    #往任务列表添加任务
    tasks_list.append(task)
#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站
gevent.joinall(tasks_list)

