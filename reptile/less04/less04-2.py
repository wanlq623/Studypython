import requests
import urllib
from bs4 import BeautifulSoup


#定义用户输入的查询电影的变量
user_name = input('请输入要下载的电影名称：').encode('gbk')

print('爬虫正在工作中，请稍等....')

#使用urllib库中的quote函数转换成url的编码
movie_name = urllib.parse.quote(user_name)

#初始url
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='

#拼装输入结果后的地址
serch_url = url + movie_name

serch_res = requests.get(serch_url)

print('返回结果：' + str(serch_res.status_code))

serch_soup = BeautifulSoup(serch_res.text,'html.parser')

movie_url = serch_soup.find('div',class_ = 'co_content8').find_all('a')[0]['href']

movie_serchurl = 'http://s.ygdy8.com' + movie_url

#根据下载地址返回一个response对象，赋值给movie_res
movie_res = requests.get(movie_serchurl)

movie_res.encoding = 'gbk'

print('返回结果：' + str(movie_res.status_code))

movie_soup = BeautifulSoup(movie_res.text,'html.parser')

movie_downurl = movie_soup.find('div',class_ ='co_content8').find('tbody').find('a')['href']

print('%s 下载地址是：%s' %(user_name.decode('gbk'),movie_downurl))