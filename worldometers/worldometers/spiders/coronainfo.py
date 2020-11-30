# -*- coding: utf-8 -*-
import scrapy


class CoronainfoSpider(scrapy.Spider):
    name = 'coronainfo'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        total_cases = response.xpath("(//div[@class='maincounter-number']/span)[1]/text()").get()
        total_deaths = response.xpath("(//div[@class='maincounter-number']/span)[2]/text()").get()
        total_recovered = response.xpath("(//div[@class='maincounter-number']/span)[3]/text()").get()

        test = response.xpath(
            "/html/body/div[2]/div[2]/div[1]/div/div[4]/div/span/text()").get()

        rows = response.xpath("(//table[@id='main_table_countries_today']/tbody)[1]/tr")
        # for row in rows:
        #     country_name = row.xpath(".//td[2]/nobr/text()").get()
        #     yield {
        #         "country: ": country_name
        #     }

        yield {
            'country_Name': test

        }
