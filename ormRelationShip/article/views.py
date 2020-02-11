from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article, Category


def index(request):
    article = Article(title='abc', content='1111')
    category = Category(name="最新文章")
    category.save()
    article.category = category
    article.save()
    return HttpResponse("success")
