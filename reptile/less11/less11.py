from gevent import monkey
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步
monkey.patch_all()
import gevent,time,requests
from gevent.queue import Queue


#记录开始时间
start = time.time()
#爬取网址列表
url_lsit = [
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/'
]
#创建队列队形，并赋值给work
work = Queue()
#遍历url_list
for url in url_lsit:
    #用put_nowait()函数可以把网址都放进队列里
    work.put_nowait(url)

#定义爬虫函数
def crawler():
    #当队列不是空的时候，就执行下面代码
    while not work.empty():
        #用get_nowait()函数把队列里面的网址取出来
        url = work.get_nowait()
        #requests.get请求url
        r = requests.get(url)
        #打印网址、队列长度、抓取请求的状态码
        print('请求网址：%s\n目前队列长度：%s\n请求网址返回的状态：%s\n----------------------'%(url,work.qsize(),r.status_code))

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
#记录结束时间
end = time.time()
#打印总时长
print('总时长：%s'%(end-start))