# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class YearPublication(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    url = scrapy.Field()

class Law(scrapy.Item):
    number = scrapy.Field()
    url = scrapy.Field()


class LeisItem(scrapy.Spider):
    pass
