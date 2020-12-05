# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AmazonPhoneSpider(CrawlSpider):
    name = 'amazon_phone'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=iphone+12&ref=nb_sb_noss']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='a-section a-spacing-none']/h2/a"), callback='parse_item',
             follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='a-last']/a"))
    )

    def parse_item(self, response):
        # 'title': response.xpath("//div[@class='a-section a-spacing-none']/h1/span/text() | //div[@class='a-section a-spacing-none']/h1/span[@id='productTitle']/text()").get(),
        # for review in response.xpath("//div[@class='a-section review aok-relative']"):
        #     yield {
        #         'url': response.url,
        #         'reviews': review.xpath(".//div[1]/div[1]/div[2]/a[2]/span/text()").getall()
        #     }
        yield {
            'url': response.url,

            'reviews': response.xpath(
                "//div[@class='a-section review aok-relative']/div[1]/div[1]/div[2]/a[2]/span/text()").getall(),
            'rev Len': len(response.xpath(
                "//div[@class='a-section review aok-relative']/div[1]/div[1]/div[2]/a[2]/span/text()").getall())
        }
