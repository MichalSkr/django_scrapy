# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from collections import Counter
import re
import json
# from scrapy_app.scrapy_app.items import ScrapyAppItem

urls = []


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://teonite.com/blog/',
    ]

    def parse(self, response):
        next_page_url = response.xpath('//*[@id="content"]/main//a/@href').extract()
        for url in next_page_url:
            if ('page' in url) and (url not in urls):
                urls.append(url)
                yield scrapy.Request(url=urljoin(response.url, url), callback=self.parse)
            else:
                yield scrapy.Request(url=urljoin(response.url, url), callback=self.parse_url)

    def parse_url(self, response):
        parsed_text = response.xpath('//*[@id="content"]/main//p/text()').extract()
        words = re.findall(r'\w+', " ".join(parsed_text))
        response_data = json.loads(response.xpath('/html/head/script/text()').extract()[0])
        yield {
            'article_link': response.url,
            'article_content': words,
            'article_author_id': response_data['author']['name'],
            'author_short': [el for el in response_data['author']['url'].split('/') if el][-1]
        }
