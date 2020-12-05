# -*- coding: utf-8 -*-
import scrapy


class Review0212Spider(scrapy.Spider):
    name = 'review_02_12'
    allowed_domains = ['www.amazon.com']
    start_urls = ['http://www.amazon.com/']

    def parse(self, response):
        pass
