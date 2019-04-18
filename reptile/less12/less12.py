from gevent import monkey
#让程序变成异步模式。
monkey.patch_all()
import gevent,requests, bs4, csv
from gevent.queue import Queue

#定义获取所有爬取网页地址的函数
def get_allurl():
    url_list = []
    for i in range(1,11):
        new = 'group/%s?'%i
        view_meun = 'http://www.boohee.com/food/view_menu?page=%s' % i
        url_list.append(view_meun)
        for n in range(1,11):
            start_url = 'http://www.boohee.com/food/'
            news = new + ('page=%s'%n)
            url_list.append(start_url+news)
    return url_list

#创建队列队形，并赋值给work
work = Queue()
#遍历url_list
for url in get_allurl():
    #用put_nowait()函数可以把网址都放进队列里
    work.put_nowait(url)

#定义crawler函数
def crawler():
    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 当队列不是空的时候，就执行下面代码
    while not work.empty():
        # 用get_nowait()函数把队列里面的网址取出来
        url = work.get_nowait()
        # requests.get请求url
        food_res = requests.get(url, headers=headers)
        # 打印网址、队列长度、抓取请求的状态码
        print('请求网址：%s\n目前队列长度：%s\n请求网址返回的状态：%s\n----------------------' % (url, work.qsize(), food_res.status_code))
        # 解析数据
        food_soup = bs4.BeautifulSoup(food_res.text, 'html.parser')
        #用find_all提取出<li class="item clearfix">标签的内容
        foods = food_soup.find_all('li',class_ = 'item clearfix')
        f_url = 'http://www.boohee.com'
        #遍历foods
        for food in foods:
            #用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素title属性的值，也就是食物名称
            food_name = food.find_all('a')[1]['title']
            #用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素href属性的值
            food_url = f_url + food.find_all('a')[1]['href']
            #用find在<li class="item clearfix">标签下，提取<p>元素，再用text方法留下纯文本，也提取出了食物的热量
            food_calorie = food.find('p').text
            #借助writerow()函数，把提取到的数据：食物名称、食物热量、食物详情链接，写入csv文件
            writer.writerow([food_name, food_calorie, food_url])
            print('食物名称：%s\n热量：%s\n链接：%s'% (food_name,food_calorie,food_url))

#调用open()函数打开csv文件，传入参数：文件名“boohee.csv”、写入模式“w”、newline=''。
csv_file= open('boohee.csv', 'w', newline='')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
#借助writerow()函数往csv文件里写入文字：食物、热量、链接
writer.writerow(['食物', '热量', '链接'])

#创建空的任务列表
tasks_list = []
#相当于创建2个爬虫
for i in range(4):
    #用gevent.spawn()函数创建执行crawler()函数的任务
    task = gevent.spawn(crawler)
    #往任务列表添加任务
    tasks_list.append(task)
#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站
gevent.joinall(tasks_list)