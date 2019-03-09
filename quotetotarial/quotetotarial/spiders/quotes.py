# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrapy.com']
    start_urls = ['http://quotes.toscrapy.com/']

    def parse(self, response):
        pass
