import scrapy,bs4
from ..items import DoubanbookItem

#定义一个爬虫类DoubanbookSpider
class DoubanbookSpider(scrapy.Spider):
    #定义爬虫名称为doubanbook
    name = 'doubanbook'
    # 定义允许爬虫爬取网址的域名
    allowed_domins = ['https://book.douban.com']
    # 定义起始网址
    start_urls = []
    #爬取2页数据
    for i in range(2):
        url = 'https://book.douban.com/top250?start=%i'%(i*25)
        start_urls.append(url)

    # parse是默认处理response的方法
    def parse(self, response):
        # 用BeautifulSoup解析response(获取书列表）
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用find_all提取<div class_="pl2">标签
        url_list = bs.find_all('div',class_ = 'pl2')
        #遍历url_list
        for url in url_list:
            #用find提取<a>标签中的href属性值
            real_url = url.find('a')['href']
            # 用yield语句把构造好的request对象传递给引擎。用scrapy.Request构造request对象。callback参数设置调用parse_book方法
            yield scrapy.Request(real_url, callback=self.parse_bookcommentsurl)

    #定义新的处理response的方法parse_bookcommentsurl
    def parse_bookcommentsurl(self,response):
        #用BeautifulSoup解析response（获取书详细）
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #用find提取<div class="mod-hd">的元素，再提取<span class="pl">的元素，再提取<a>标签的href元素值
        bookcomments_url = bs.find('div',class_ = 'mod-hd').find('span',class_ ='pl').find('a')['href']
        # 用yield语句把构造好的request对象传递给引擎。用scrapy.Request构造request对象。callback参数设置调用parse_bookcomments方法
        yield scrapy.Request(bookcomments_url,callback=self.parse_bookcomments)

    # 定义新的处理response的方法parse_bookcomments
    def parse_bookcomments(self,response):
        # 用BeautifulSoup解析response（获取短评列表）
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #用find_all提取<p class = "pl2 side-bar-link">元素，在提取<a>标签的元素
        book_name = bs.find_all('p', class_='pl2 side-bar-link')[1].find('a').text
        #用find_all提取<div class="comment">的元素
        comments_lsit = bs.find_all('div', class_='comment')
        #遍历comments_lsit
        for comments in comments_lsit:
            #实例化DoubanbookItem这个类
            item = DoubanbookItem()
            #把书名放回DoubanbookItem类的book_name属性里
            item['book_name'] = book_name
            # 把评论ID放回DoubanbookItem类的comment_info属性里
            item['comment_info'] = comments.find('span', class_='comment-info').find('a').text
            # 把评论内容放回DoubanbookItem类的comment_content属性里
            item['comment_content'] = comments.find('span', class_='short').text
            #打印
            print(item['book_name'],item['comment_info'],item['comment_content'])
            # 用yield语句把构造好的item传递给引擎
            yield item