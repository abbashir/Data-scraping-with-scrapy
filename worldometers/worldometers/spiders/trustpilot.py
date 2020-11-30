# -*- coding: utf-8 -*-
import scrapy


class TrustpilotSpider(scrapy.Spider):
    name = 'trustpilot'
    allowed_domains = ['www.trustpilot.com']
    start_urls = ['https://www.trustpilot.com/categories/internet_software/']

    def parse(self, response):
        for company in response.xpath("//div[@class='styles_categoryBusinessListWrapper__2H2X5']/a"):
            yield {
                "company_name": company.xpath(".//div/text()").get(),
                "company_url": response.urljoin(company.xpath(".//@href").get()),
                "review_quantity": company.xpath(".//div[@class='styles_textRating__19_fv']/text()").get(),
            }
        next_page = response.urljoin(response.xpath(
            "//a[@class='pagination-link_paginationLinkNormalize__dzIry pagination-link_paginationLinkNext__1n3P4']/@href").get())

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
