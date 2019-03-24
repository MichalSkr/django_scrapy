# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from collections import Counter
import re
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
        # print(response.url)
        parsed_text = response.xpath('//*[@id="content"]/main//p/text()').extract()
        print(response.xpath("//span[contains(@class,'author')]/h4/text()").extract()[0])
        author = response.xpath("//span[contains(@class,'author')]/h4/text()").extract()[0] if\
        response.xpath("//span[contains(@class,'author')]/h4/text()").extract()[0] else None
        words = re.findall(r'\w+', " ".join(parsed_text))
        for element in Counter(filter(None, words)): #.most_common(10):
            yield {
                'word': element[0],
                'number': element[1],
                'author': author
            }
