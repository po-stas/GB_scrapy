# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python&page=0']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancies = response.xpath('//a[@class="bloko-link HH-LinkModifier"]/@href')
        for vacancy in vacancies:
            yield response.follow(vacancy.extract(), callback=self.vacancy_parse)

    @staticmethod
    def vacancy_parse(responce:HtmlResponse):
        result = dict()
        result['title'] = ''.join(responce.xpath('//div[contains(@class, "vacancy-title")]/h1/span/text()').extract())
        if not result['title']:
            result['title'] = ''.join(responce.xpath('//div[contains(@class, "vacancy-title")]/h1/text()').extract())

        result['salary'] = ''.join(responce.xpath('//p[@class="vacancy-salary"]/text()').extract())
        result['link'] = responce.url
        yield JobparserItem(result)
