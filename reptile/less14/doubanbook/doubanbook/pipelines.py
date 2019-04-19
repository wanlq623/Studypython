# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl

#定义一个DoubanbookPipeline类，负责处理item
class DoubanbookPipeline(object):
    # 初始化函数，当类实例化时这个方法会自动启动
    def __init__(self):
        # 创建工作簿
        self.wb = openpyxl.Workbook()
        # 定位活动表
        self.ws = self.wb.active
        # 用append()函数添加表头
        self.ws.append(['书名', '评论ID', '评论内容'])

    #process_item是默认的处理item的方法，就像parse是默认处理response的方法
    def process_item(self, item, spider):
        # 把书名、评论ID、评论内容都写成列表的形式，赋值给line
        line = [item['book_name'], item['comment_info'], item['comment_content']]
        # 用append函数把书名、评论ID、评论内容的数据都添加进表格
        self.ws.append(line)
        # 将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度
        return item

    # close_spider是当爬虫结束运行时，这个方法就会执行
    def close_spider(self, spider):
        # 保存文件
        self.wb.save('./doubanbooks.xlsx')
        # 关闭文件
        self.wb.close()