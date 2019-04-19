# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 定义书名的数据属性
    book_name = scrapy.Field()
    # 定义评论ID的数据属性
    comment_info = scrapy.Field()
    # 定义评论内容的数据属性
    comment_content = scrapy.Field()