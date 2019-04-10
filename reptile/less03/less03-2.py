import requests
from bs4 import BeautifulSoup

#第一题
# 返回一个response对象，赋值给res
res = requests.get('http://books.toscrape.com/')

#打印请求状态，返回200为请求正常
print('返回状态：' + str(res.status_code))

# 把res解析为字符串
html = res.text

# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')

#通过匹配属性class='nav nav-list'提取出数据后，再提取的数据总在匹配标签<li>再次提取数据
items = soup.find(class_ = 'nav nav-list').find_all('li')

#print(items)
# 遍历列表items
for item in items:

    # 在列表中的每个元素里，匹配标签<a>提取出数据
    book_type = item.find('a')

    # 打印书籍类型，通过strip()函数去除空格和换行符
    print(book_type.text.strip())



#第二题
# 返回一个response对象，赋值给res
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')

#打印请求状态，返回200为请求正常
print('返回状态：' + str(res.status_code))

# 把res解析为字符串
html = res.text

# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')

#通过匹配属性class='col-xs-6 col-sm-4 col-md-3 col-lg-3'提取出数据
items = soup.find_all(class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

#print(items)
# 遍历列表items
for item in items:

    #在列表中的每个元素里，匹配标签<h3>提取出数据后，再匹配标签<a>提取出数据，再获取属性为title的值
    book_name = item.find('h3').find('a')['title']

    #在列表中的每个元素里，匹配属性class='price_color'提取出数据，并使用text文本方式
    book_price = item.find(class_ = 'price_color').text

    # 在列表中的每个元素里，匹配标签<p>和属性class='star-rating'提取出数据，再获取属性为class的值并从第1个元素进行切片
    book_star = item.find('p',class_ = 'star-rating')['class'][1]

    #打印书名、价格、星级
    print('书名：%s\n价格：%s\n星级：%s星\n' % (book_name,book_price,book_star))

