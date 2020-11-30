# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'GDP'
    allowed_domains = ['www.worldpopulationreview.com']  # remove: /countries/countries-by-national-debt
    start_urls = ['https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("(//table[@class='jsx-1487038798 table table-striped tp-table-body'])/tbody/tr")

        for row in rows:
            country_name = row.xpath(".//td[1]/a/text()").get()
            gdp = row.xpath(".//td[2]/text()").get()

            yield {
                'country_name': country_name,
                'GDP': gdp
            }
