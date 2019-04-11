import requests
from bs4 import BeautifulSoup

#翻页循环获取数据
for i in range(1,11):
    #url中页面的参数赋值
    start = (i-1) * 25
    #拼装url
    url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
    #返回一个response对象，赋值给movie_res
    movie_res = requests.get(url)

    #打印请求状态，返回200为请求正常
    print('返回状态：' + str(movie_res.status_code))

    # 把网页解析为BeautifulSoup对象
    movie_soup = BeautifulSoup(movie_res.text,'html.parser')

    #通过匹配标签ol，属性class='grid_view'提出元素，再提取后的元素中在匹配标签div,属性class='item'，查找出全部符合条件的数据
    movie_list = movie_soup.find('ol',class_='grid_view').find_all('div',class_='item')

    #遍历movie_list
    for movie in movie_list:

        #通过匹配标签em，获取数据，并通过text形式展示
        movie_number = movie.find('em').text

        #通过匹配标签div，属性class='info'获取数据，再获取到的数据中通过匹配标签a获取二次数据，在二次数据获取后，通过匹配属性class='title'获取数据，通过text展示
        movie_name = movie.find('div',class_ = 'info').find('a').find(class_ = 'title').text

        #通过匹配标签div，属性class='star'获取数据，获取数据后通过匹配属性class='rating_num'获取数据，通过text展示
        movie_star = movie.find('div',class_ = 'star').find(class_ = 'rating_num').text

        #通过匹配标签p，属性class='quote'获取数据
        movie_recommend = movie.find('p',class_ ='quote')

        # 通过匹配标签div，属性class='info'获取数据，再获取到的数据中匹配标签a获取二次数据，通过获取href来获取链接
        movie_url = movie.find('div',class_ = 'info').find('a')['href']

        #异常处理
        try:
            print('序号：%s\n电影名称：%s\n评分：%s\n推荐语：%s\n链接：%s\n' % (movie_number,movie_name,movie_star,movie_recommend.text.strip(),movie_url))

        #获取到AttributeError异常，执行后面的语句
        except AttributeError:
            print('序号：%s\n电影名称：%s\n评分：%s\n推荐语：\n链接：%s\n' % (movie_number, movie_name, movie_star, movie_url))



#第二种获取方案

#翻页循环获取数据
for i in range(1,11):
    #url中页面的参数赋值
    start = (i-1) * 25
    #拼装url
    url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
    #返回一个response对象，赋值给movie_res
    movie_res = requests.get(url)
    # 打印请求状态，返回200为请求正常
    print('返回状态：' + str(movie_res.status_code))
    # 把网页解析为BeautifulSoup对象
    movie_soup = BeautifulSoup(movie_res.text,'html.parser')
    all_movies = movie_soup.find('ol').find_all('li')
    for movies in all_movies:
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
            remark = '没有推荐语'
        #获取链接
        url = movies.find('div',class_ = 'info').find('a')['href']
        print('序号：%s\n电影名称：%s\n评分：%s\n推荐语：%s\n链接：%s\n'%(em,name,scores,remark,url))





