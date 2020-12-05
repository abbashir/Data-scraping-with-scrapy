# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import requests
import xlrd


class ReviewSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://amazon.com/']

    def parse(self, response):
        excel_data = pd.read_excel('asin.xlsx')
        for asin in excel_data['ASIN'].tolist():
            link = '/dp/' + asin

            yield response.follow(url=link, callback=self.parse_getreview, meta={'asin': asin})

    def parse_getreview(self, response):
        reviews = response.xpath("//div[@class='a-section review aok-relative']")

        if reviews:
            for review in reviews:
                yield {
                    'ASIN': response.request.meta['asin'],
                    'StarRating': (review.xpath(".//div/div/div[2]/a[1]/i/span/text()").get())[0],
                    'Title': review.xpath(".//div/div/div[2]/a[2]/span/text()").get(),
                    'ReviewLink': response.urljoin(review.xpath(".//div/div/div[2]/a[2]/@href").get()),
                    'ReviewDate': (review.xpath(".//div/div/span[1]/text()").get()).partition("on")[2],
                    'AuthorName': review.xpath(".//div/div/div/a/div[2]/span/text()").get(),
                    'VerifiedPurchase': review.xpath(
                        ".//div/div/div[3]/span[@class='a-size-mini a-color-state a-text-bold']/text()").get(),
                    'ReviewText': review.xpath("normalize-space(.//div/div/div[4]/span/div/div/span/text())").get()
                }
        else:
            print("Review Not found ID: ", response.request.meta['asin'])
            yield {
                'ASIN': response.request.meta['asin']
            }
