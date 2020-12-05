# -*- coding: utf-8 -*-
import scrapy


class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/']

    def parse(self, response):
        pass
