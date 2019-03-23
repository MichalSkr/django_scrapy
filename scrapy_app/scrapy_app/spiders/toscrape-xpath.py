# -*- coding: utf-8 -*-
import scrapy
from collections import Counter
import re
# from scrapy_app.scrapy_app.items import ScrapyAppItem


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://teonite.com/blog/',
    ]

    def parse(self, response):

        parsed_text = response.xpath('//*[@id="content"]/main//p/text()').extract()
        words = re.findall(r'\w+', " ".join(parsed_text))
        for element in Counter(filter(None, words)).most_common(10):
            yield {
                'word': element[0],
                'number': element[1],
            }

        # next_page_url = response.xpath('//*[@id="content"]/main//p/a/@href').extract_first()
        # print('\n\n\n\nNEXT PAGE:',next_page_url,'\n\n\n\n')
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
