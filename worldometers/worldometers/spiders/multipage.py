# -*- coding: utf-8 -*-
import scrapy


class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='p-title-block']"):
            yield {
                'name': (product.xpath(".//div[@class='p-title']/a/text()").get()).replace('\n', '').replace(' ', ''),
                'price': product.xpath(".//div[@class='p-price']/div[1]/span/text()").get(),
                'url': product.xpath(".//div[@class='p-title']/a/@href").get()
            }
        # yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse)

        next_page = response.xpath("//a[@class='page-link']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
