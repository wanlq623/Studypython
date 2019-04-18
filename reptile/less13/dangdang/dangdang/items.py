# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义一个类DangdangItem，继承来自scrapy.Item
class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 定义书名的数据属性
    title = scrapy.Field()
    # 定义作者的数据属性
    author = scrapy.Field()
    # 定义价格的数据属性
    price = scrapy.Field()

