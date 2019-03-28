from django.db import models


class Author(models.Model):
    author_fullname = models.CharField(max_length=100)
    author_short = models.CharField(max_length=100)

    objects = models.Manager()


class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    article_link = models.CharField(max_length=200)
    article_content = models.TextField()

    objects = models.Manager()
