# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os
import codecs
from leis.items import YearPublication, Law, LawText
from scrapy.spiders import Spider
from scrapy.http import Request

class LeisItem(scrapy.Spider):
    # define the fields for your item here like:
    name = 'leis'
    start_urls = [
            'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias'
            ]

    def parse(self, response):
         links = response.xpath("//*[@id='parent-fieldname-text']/table/tbody/tr/th/a")
         #| //*[@id='parent-fieldname-text']/table/tbody/tr/th/strong/a/").extract()
         if links:
             for l in links:
                 url = l.xpath("@href").extract()[0]
                 year = l.select('text()').extract()
                 if len(year) > 0:
                     item = YearPublication()
                     item["year"] = year[0]
                     item["url"] =  url
                     if item:
                         yield Request(url=url, callback=self.parse_page_year, meta={'item': item})

    def parse_page_year(self, response):
        item_year = response.meta['item']
        print(item_year)
        links = response.xpath("//*[@id='visao2']/table/tr/td/a")
        if links:
            for l in links:
                url = l.xpath("@href").extract()[0]
                if url:
                    item = Law()
                    item["url"] = url
                    item["number"] = os.path.splitext(os.path.basename(url))[0]
                    item["year"] = item_year["year"]
                    yield Request(url=url, callback=self.parse_page_law, meta={'item': item})

    def parse_page_law(self, response):
        item_law = response.meta['item']
        print(item_law)
        law = response.xpath("//body//text()").extract()
        if law:
            item = LawText()
            item["url"] = item_law["url"]
            item["text"] = law
            item["number"] = item_law["number"]
            item["year"] = item_law["year"]
            return item
