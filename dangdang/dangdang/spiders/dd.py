# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@name='itemlist-title']/@title").extract()
        item["link"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        # item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item
        #翻页
        for i in range(2,10):
            url = 'http://search.dangdang.com/?key=python&act=input&page_index={}'.format(i)
            yield Request(url,callback=self.parse)
