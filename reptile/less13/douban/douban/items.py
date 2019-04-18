# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义一个类DoubanItem，继承来自scrapy.Item
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义书名的数据属性
    title = scrapy.Field()
    #定义出版信息的数据属性
    publish = scrapy.Field()
    #定义评分的数据属性
    score = scrapy.Field()
