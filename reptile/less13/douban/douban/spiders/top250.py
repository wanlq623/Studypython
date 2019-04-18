import scrapy,bs4
from ..items import DoubanItem

#定义一个爬虫类DoubanSpider
class DoubanSpider(scrapy.Spider):
    #定义爬虫名字为douban
    name = 'douban'
    #定义允许爬虫爬取的网址域名
    allowed_domains = ['https://book.douban.com']
    #定义起始网址列表
    start_urls = []
    #爬取3页数据
    for i in range(3):
        url = 'https://book.douban.com/top250?start=%s'%(i*25)
        start_urls.append(url)

    #parse是默认处理response的方法
    def parse(self,response):
        #用BeautifulSoup解析网页
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        #用find_all提取<tr class="item">元素，这个元素里含有书籍信息
        datas = soup.find_all('tr',class_ = 'item')
        #遍历datas
        for data in datas:
            #实例化类DoubanItem
            item = DoubanItem()
            #获取书名,并把这个数据放回DoubanItem类的title属性里
            item['title'] = data.find_all('a')[1]['title']
            #获取出版信息,并把这个数据放回DoubanItem类的publish属性里
            item['publish'] = data.find('p',class_ = 'pl').text
            #获取评分,并把这个数据放回DoubanItem类的score属性里
            item['score'] = data.find('span',class_ = 'rating_nums').text
            #打印
            print('书名：%s\n出版信息：%s\n评分：%s\n----------'%(item['title'],item['publish'],item['score']))
            # yield item是把获得的item传递给引擎
            yield item