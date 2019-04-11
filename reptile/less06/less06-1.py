import requests
from bs4 import BeautifulSoup
import openpyxl

'''
目前定义函数的方法执行效率过慢（下面这段代码），需要寻求性能优化
'''
#定义爬虫获取网页的函数
def get_web(url):
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

#爬取数据并写入文件函数
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
    # 创建工作簿
    wb = openpyxl.Workbook()
    # 获取工作簿的活动表
    sheet = wb.active
    # 工作表明码为song
    sheet.title = 'movies'
    # 把'序号','电影名称','评分','推荐语','链接'分别写入到'A1','B1','C1','D1','E1'单元格中
    sheet['A1'] = '序号'
    sheet['B1'] = '电影名称'
    sheet['C1'] = '评分'
    sheet['D1'] = '推荐语'
    sheet['E1'] = '链接'

    for i in range(1,11):
        #url中页面的参数赋值
        start = (i-1) * 25
        #拼装url
        web_url = 'https://movie.douban.com/top250?start=%s&filter=' % start
        #定义all_movie变量并调用get_web()函数赋值
        all_movie = get_web(web_url)
        #调用get_writer()函数
        get_writer(all_movie)
        #根据writer_movies列表逐行写入文件
        for i in  range(len(get_writer(all_movie))):
            em = get_writer(all_movie)[i][0]
            name = get_writer(all_movie)[i][1]
            socers = get_writer(all_movie)[i][2]
            remark = get_writer(all_movie)[i][3]
            url = get_writer(all_movie)[i][4]
            sheet.append([em, name, socers, remark, url])
    #保存文件
    wb.save('movie.xlsx')








'''
下面这段代码执行效率正常，但是未做函数封装
'''
# #创建工作簿
# wb = openpyxl.Workbook()
# #获取工作簿的活动表
# sheet = wb.active
# #工作表明码为song
# sheet.title = 'movies'
# #把'序号','电影名称','评分','推荐语','链接'分别写入到'A1','B1','C1','D1','E1'单元格中
# sheet['A1'] = '序号'
# sheet['B1'] = '电影名称'
# sheet['C1'] = '评分'
# sheet['D1'] = '推荐语'
# sheet['E1'] = '链接'
#
# #翻页循环获取数据
# for i in range(1,11):
#     #url中页面的参数赋值
#     start = (i-1) * 25
#     #拼装url
#     url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
#     #返回一个response对象，赋值给movie_res
#     movie_res = requests.get(url)
#     #打印请求状态，返回200为请求正常
#     print('返回状态：' + str(movie_res.status_code))
#     # 把网页解析为BeautifulSoup对象
#     movie_soup = BeautifulSoup(movie_res.text,'html.parser')
#     #通过匹配标签ol，属性class='grid_view'提出元素，再提取后的元素中在匹配标签div,属性class='item'，查找出全部符合条件的数据
#     movie_list = movie_soup.find('ol',class_='grid_view').find_all('div',class_='item')
#     #遍历movie_list
#     for movie in movie_list:
#         #通过匹配标签em，获取数据，并通过text形式展示
#         movie_number = movie.find('em').text
#         #通过匹配标签div，属性class='info'获取数据，再获取到的数据中通过匹配标签a获取二次数据，在二次数据获取后，通过匹配属性class='title'获取数据，通过text展示
#         movie_name = movie.find('div',class_ = 'info').find('a').find(class_ = 'title').text
#         #通过匹配标签div，属性class='star'获取数据，获取数据后通过匹配属性class='rating_num'获取数据，通过text展示
#         movie_star = movie.find('div',class_ = 'star').find(class_ = 'rating_num').text
#
#         try:
#             # 通过匹配标签p，属性class='quote'获取数据
#             movie_recommend = movie.find('p',class_ ='quote').text
#         except AttributeError:
#             movie_recommend = ''
#         # 通过匹配标签div，属性class='info'获取数据，再获取到的数据中匹配标签a获取二次数据，通过获取href来获取链接
#         movie_url = movie.find('div',class_ = 'info').find('a')['href']
#         #写入文件
#         sheet.append([movie_number,movie_name,movie_star,movie_recommend,movie_url])
# #保存文件
# wb.save('movies.xlsx')
