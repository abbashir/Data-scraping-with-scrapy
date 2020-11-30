# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookListSpider(CrawlSpider):
    name = 'book_list'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'url': response.url
        }
