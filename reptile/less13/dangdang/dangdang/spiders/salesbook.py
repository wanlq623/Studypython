import scrapy,bs4
from ..items import DangdangItem

##定义一个爬虫类DangdangSpider
class DangdangSpider(scrapy.Spider):
    # 定义爬虫名字为dangdang
    name = 'dangdang'
    # 定义允许爬虫爬取的网址域名
    allowed_domains = ['http://bang.dangdang.com']
    # 定义起始网址列表
    start_urls = []
    # 爬取3页数据
    for i in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%s' % i
        start_urls.append(url)

    #parse是默认处理response的方法
    def parse(self, response):
        # 用BeautifulSoup解析网页
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        #用find提取<ul class="bang_list clearfix bang_list_mode">元素,再用find_all提取<li>标签元素，这个元素里含有书籍信息
        datas = soup.find('ul',class_ = 'bang_list clearfix bang_list_mode').find_all('li')
        #遍历datas
        for data in datas:
            #实例化类DangdangItem
            item = DangdangItem()
            #获取书名,并把这个数据放回DangdangItem类的title属性里
            item['title'] = data.find('div',class_ = 'name').find('a').text
            #获取作者,并把这个数据放回DangdangItem类的title属性里
            item['author'] = data.find('div',class_ = 'publisher_info').find('a').text
            #获取价格,并把这个数据放回DangdangItem类的title属性里
            item['price'] = data.find('div',class_ = 'price').find('span',class_ = 'price_n').text
            #打印结果
            print('书名：%s\n作者：%s\n价格：%s\n--------------'%(item['title'],item['author'],item['price']))
            #yield item是把获得的item传递给引擎
            yield item

