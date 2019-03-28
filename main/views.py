from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from main.models import Author, Article
from main.counter import count


@api_view()
def list_authors(request):
    authors = dict(Author.objects.all().values_list('author_short', 'author_fullname'))

    if not authors:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(authors)


@api_view()
def words(request):
    content = count(Article.objects.all().values_list('article_content', flat=True))
    if not content:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(content)


@api_view()
def words_by_authors(request, author):
    content = count(
        Article.objects.filter(article_author__author_short=author).values_list('article_content', flat=True))

    if not content:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(content)
