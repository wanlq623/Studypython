import requests
from bs4 import BeautifulSoup

# 返回一个response对象，赋值给res
res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')

#打印请求状态，返回200为请求正常
print('返回状态：' + str(res.status_code))

# 把res解析为字符串
html = res.text

#把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')

# 通过匹配属性class='comment-body'提取出我们想要的元素
items = soup.find_all(class_ = 'comment-body' )

#print(items)
# 遍历列表items
for item in items:

    #print(item)
    # 在列表中的每个元素里，匹配属性class='fn'提取出数据
    name = item.find(class_ = 'fn')

    # 在列表中的每个元素里，匹配标签<p>提取出数据
    comment = item.find('p')

    # 在列表中的每个元素里，匹配标签<time>提取出数据
    times = item.find('time')

    #打印名字-评论时间-评论内容，strip()函数可以去除空格和换行符
    print(name.text,'-',times.text.strip(),'-',comment.text,'\n')
