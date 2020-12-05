# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoronainfoSpider(scrapy.Spider):
    name = 'coronainfo'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.worldometers.info/coronavirus/")

        # rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        # rur_tab[4].click()

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for data in resp.xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[@class='odd' or @class='even']"):
            yield {
                'country_name': data.xpath(".//td[2]/a/text()").get(),
                'total_case': data.xpath(".//td[3]/text()").get(),
                'new_case': data.xpath(".//td[4]/text()").get(),
                'total_death': data.xpath(".//td[5]/text()").get(),
            }
