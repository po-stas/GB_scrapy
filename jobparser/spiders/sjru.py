# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bc%5D%5B0%5D=1']

    def parse(self, response):
        next_page = response.css('a.f-test-button-dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancies = response.xpath('//a[contains(@class, "_1QIBo")]/@href')
        for vacancy in vacancies:
            yield response.follow('https://www.superjob.ru' + vacancy.extract(), callback=self.vacancy_parse)

    @staticmethod
    def vacancy_parse(responce:HtmlResponse):
        result = dict()
        result['title'] = responce.xpath('//h1[@class="_3mfro rFbjy s1nFK _2JVkc"]//text()').extract()
        result['salary'] = responce.xpath('//span[@class="_3mfro _2Wp8I ZON4b PlM3e _2JVkc"]//text()').extract()
        result['link'] = responce.url
        yield JobparserItem(result)
