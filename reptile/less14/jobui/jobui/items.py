# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 定义公司的数据属性
    company = scrapy.Field()
    # 定义招聘岗位的数据属性
    job_title = scrapy.Field()
    # 定义工作地点的数据属性
    job_city = scrapy.Field()
    # 定义招聘要求的数据属性
    job_required = scrapy.Field()
