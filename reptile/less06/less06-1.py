import requests
from bs4 import BeautifulSoup
import openpyxl

#创建工作簿
wb = openpyxl.Workbook()
#获取工作簿的活动表
sheet = wb.active
#工作表明码为song
sheet.title = 'movies'
#把'序号','电影名称','评分','推荐语','链接'分别写入到'A1','B1','C1','D1','E1'单元格中
sheet['A1'] = '序号'
sheet['B1'] = '电影名称'
sheet['C1'] = '评分'
sheet['D1'] = '推荐语'
sheet['E1'] = '链接'

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

        try:
            # 通过匹配标签p，属性class='quote'获取数据
            movie_recommend = movie.find('p',class_ ='quote').text
        except AttributeError:
            movie_recommend = ''
        # 通过匹配标签div，属性class='info'获取数据，再获取到的数据中匹配标签a获取二次数据，通过获取href来获取链接
        movie_url = movie.find('div',class_ = 'info').find('a')['href']
        #写入文件
        sheet.append([movie_number,movie_name,movie_star,movie_recommend,movie_url])
#保存文件
wb.save('movies.xlsx')
