# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeisItem(scrapy.Item):
    # define the fields for your item here like:
    name = 'leis'
    start_urls = [
            'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias'
            ]

    def parse(self, response):
        a = response.xpath("//*[@id='parent-fieldname-text']/table/tbody/tr/th/a/@href | //*[@id='parent-fieldname-text']/table/tbody/tr/th/strong/a/@href").extract()
