# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
import re


class SjruSpider(scrapy.Spider):
    name = 'superjob.ru'
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
        result['title'] = ''.join(responce.xpath('//h1[@class="_3mfro rFbjy s1nFK _2JVkc"]//text()').extract())
        salary = ''.join(responce.xpath('//span[@class="_3mfro _2Wp8I ZON4b PlM3e _2JVkc"]//text()').extract())
        salary = salary.replace('\xa0—\xa0', '-')
        result['salary'] = re.sub(r'(\d+)\xa0(\d+)', r'\1\2', salary).replace('\xa0', ' ')
        result['link'] = responce.url
        yield JobparserItem(result)
