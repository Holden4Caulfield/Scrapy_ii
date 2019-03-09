# -*- coding: utf-8 -*-
import scrapy
from dmmspider.items import  DmmspiderItem

class DmmseeSpider(scrapy.Spider):
    name = 'dmmsee'
    allowed_domains = ['www.dmmsee.net']
    start_urls = ['https://www.dmmsee.net/']

    def __init__(self):
        self.page=10

    def parse(self, response):
        item = DmmspiderItem()
        movies=response.css('div.item')
        for movie in movies:
            item['name']= movie.css('span::text').extract_first()
            yield item

        next_page=response.css('#next::attr(href)').extract_first()
        # print(next_page)
        # for i in range(5):
        #     print(i)

        if next_page is not None:  # 判断是否存在下一页
            if self.page>0:
                self.page=self.page-1
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页

        pass
