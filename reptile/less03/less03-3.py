import requests
from bs4 import BeautifulSoup

# 返回一个response对象，赋值给res
res = requests.get('https://spidermen.cn/')

#打印请求状态，返回200为请求正常
print('返回状态：' + str(res.status_code))

# 把res解析为字符串
html = res.text

# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')

# 通过匹配属性class='site-main'，<header>标签，提取出我们想要的元素
items = soup.find(class_ = 'site-main').find_all('header')

#print(items)
# 遍历列表items
for item in items:

    # 在列表中的每个元素里，匹配标签<h2>提取出数据，并使用text文本方式
    title = item.find('h2').text

    # 在列表中的每个元素里，匹配标签<a>提取出数据后获取属性为'href'的值
    url = item.find('a')['href']

    # 在列表中的每个元素里，匹配标签属性class='entry-date published'提取出数据，并使用text文本方式
    book_times = item.find(class_ = 'entry-date published').text

    #打印三个获取到的元素值
    print('标题：%s \n时间：%s \n链接：%s'%(title,book_times,url))