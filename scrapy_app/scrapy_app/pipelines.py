# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class ScrapyAppPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'michalsklyar'
        password = '' # your password
        database = 'scraped_data'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        self.cur.execute("delete from main_content")

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into main_content(word,number) values(%s,%s)", (item['word'], item['number']))
        self.connection.commit()
        return item