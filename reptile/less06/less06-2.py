import csv
import requests
from bs4 import BeautifulSoup

#定义爬虫获取网页的函数
def get_web(start):
    #请求url
    url = 'https://movie.douban.com/top250?start=%s&filter=' % start
    #模拟请求头文件
    header = {
        'User - Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #返回一个response对象，赋值给movie_res
    res_movie = requests.get(url,headers = header)
    #打印请求状态，返回200为请求正常
    print('返回状态：' + str(res_movie.status_code))
    #把网页解析为BeautifulSoup对象
    movie_soup = BeautifulSoup(res_movie.text,'html.parser')
    #匹配标签ol获取数据，再匹配标签li获取全部数据
    movies = movie_soup.find('ol').find_all('li')
    #暂存数据
    return movies

#爬取数据并写入数据函数
def get_writer(all_movie):
    #写入数据列表
    writer_movies = []
    #遍历all_movie
    for movies in all_movie:
        #获取序号
        em = movies.find('em').text
        #获取电影名称
        name = movies.find('span').text
        #获取评分
        scores = movies.find_all('span',class_='rating_num')[0].text
        #获取推荐语
        remarks = movies.find_all('span',class_='inq')
        if remarks:
            remark = remarks[0].text.strip()
        else:
            remark = '此影片没有推荐语'
        #获取链接
        url = movies.find('div',class_ = 'info').find('a')['href']
        #print('序号：%s\n电影名称：%s\n评分：%s\n推荐语：%s\n链接：%s\n'%(em,name,scores,remark,url))
        writer_movies.append([em,name,scores,remark,url])
    return writer_movies

#调用函数
if __name__ == "__main__":
    #创建对象csv_file 打开movies.csv文件并设置为追加a模式
    csv_file = open('movies.csv', 'a', newline='')
    writer = csv.writer(csv_file)
    list1 = ['序号', '电影名称', '评分', '推荐语', '链接']
    #写入表头
    writer.writerow(list1)

    for i in range(1,11):
        #url中页面的参数赋值
        start = (i-1) * 25
        #定义all_movie变量并调用get_web()函数赋值
        all_movie = get_web(start)
        #调用get_writer()函数并赋值给变量movie_list
        movie_list = get_writer(all_movie)
        #逐行写入文件
        for i in range(len(movie_list)):
            datalist = movie_list[i]
            writer.writerow(datalist)
    #文件关闭
    csv_file.close()
