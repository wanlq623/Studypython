#自己写的
import requests
from bs4 import BeautifulSoup

# 返回一个response对象，赋值给res
res = requests.get('http://www.xiachufang.com/explore/')

#打印请求状态，返回200为请求正常
print('返回状态：' + str(res.status_code))

# 把res解析为字符串
html = res.text

# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')

#print(soup)
#通过匹配属性class='info pure-u'，提取出我们想要的元素
items = soup.find_all(class_ = 'info pure-u')

#print(items)
web_url = 'http://www.xiachufang.com'

#定义一个空的列表存放菜谱
food_list = []

#遍历列表items
for item in items:
    food_name = item.find('a').text[17:-13]
    food_url = web_url + item.find('a')['href']
    food_value = item.find(class_ = 'ing ellipsis').text[1:-1]
    food_list.append([food_name,food_url,food_value])
print(food_list)

#教程答案1
# import requests
# # 引用requests库
# from bs4 import BeautifulSoup
# # 引用BeautifulSoup库
#
# res_foods = requests.get('http://www.xiachufang.com/explore/')
# # 获取数据
# bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# # 解析数据
# list_foods = bs_foods.find_all('div',class_='info pure-u')
# # 查找最小父级标签
#
# list_all = []
# # 创建一个空列表，用于存储信息
#
# for food in list_foods:
#
#     tag_a = food.find('a')
#     # 提取第0个父级标签中的<a>标签
#     name = tag_a.text[17:-13]
#     # 菜名，使用[17:-13]切掉了多余的信息
#     URL = 'http://www.xiachufang.com'+tag_a['href']
#     # 获取URL
#     tag_p = food.find('p',class_='ing ellipsis')
#     # 提取第0个父级标签中的<p>标签
#     ingredients = tag_p.text[1:-1]
#     # 食材，使用[1:-1]切掉了多余的信息
#     list_all.append([name,URL,ingredients])
#     # 将菜名、URL、食材，封装为列表，添加进list_all
#
# print(list_all)
# # 打印

#教材答案2
# import requests
# # 引用requests库
# from bs4 import BeautifulSoup
# # 引用BeautifulSoup库
#
# res_foods = requests.get('http://www.xiachufang.com/explore/')
# # 获取数据
# bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# # 解析数据
#
# tag_name = bs_foods.find_all('p',class_='name')
# print(tag_name)
# # 查找包含菜名和URL的<p>标签
# tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# # 查找包含食材的<p>标签
# list_all = []
# # 创建一个空列表，用于存储信息
# for x in range(len(tag_name)):
# # 启动一个循环，次数等于菜名的数量
#     list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
#     # 提取信息，封装为列表。注意此处[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
#     list_all.append(list_food)
#     # 将信息添加进list_all
# print(list_all)
# # 打印