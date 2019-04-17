from gevent import monkey
#让程序变成异步模式。
monkey.patch_all()
import gevent,requests, bs4, csv
from gevent.queue import Queue

#定义获取所有爬取网页地址的函数
def get_allurl():
    url_list = []
    for i in range(1,11):
        new = 'grop/%s?'%i
        view_meun = 'http://www.boohee.com/food/view_menu?page=%s' % i
        url_list.append(view_meun)
        for n in range(1,11):
            start_url = 'http://www.boohee.com/food/'
            news = new + ('page=%s'%n)
            url_list.append(start_url+news)
    return url_list