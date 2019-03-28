# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from main.models import Article, Author


class ScrapyAppPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'michalsklyar'
        password = ''  # your password
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname, port=5432, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        list_of_authors_in_db = list(Author.objects.all().values_list('author_short', flat=True))
        links_of_articles_in_db = list(Article.objects.all().values_list('article_link', flat=True))

        if not item['article_link'] in links_of_articles_in_db:
            article = Article()
            article.article_link = item['article_link']
            article.article_content = item['article_content']
            if item['author_short'] in list_of_authors_in_db:
                article_author = Author.objects.get(author_short=item['author_short'])
            else:
                # If not, create new DB Authors item and then assign.
                article_author = Author(author_fullname=item['article_author_id'],
                                    author_short=item['author_short'])
            article.article_author = article_author
            article_author.save()
            article.save()
            self.connection.commit()
            return item