# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ScrapymysqlItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = Field()  # 标签字段
    cont = Field()  # 名言内容
    pass
