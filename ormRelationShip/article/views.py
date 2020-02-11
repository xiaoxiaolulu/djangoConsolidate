from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from article.models import Article, Category, Tag


def index(request):
    article = Article(title='abc', content='1111')
    category = Category(name="最新文章")
    category.save()
    article.category = category
    article.save()
    return HttpResponse("success")


def del_view(request):

    cate = Category.objects.get(pk=1)
    cate.delete()
    return HttpResponse('success')


def one_to_many_view(request):
    # ar = Article(title='钢铁是', content='asn')
    # ca = Category.objects.first()
    # ar.category = ca
    # ar.save()
    # return HttpResponse('success')

    # 获取分类下的所有文章
    # ca = Category.objects.first()
    # print(ca.article_set.first())

    # ca = Category.objects.first()
    # print(ca.articles.first())

    ca = Category.objects.first()
    ar = Article(title='12', content='222')
    ca.articles.add(ar, bulk=False)
    return HttpResponse('success')


def many_to_many_view(request):

    art = Article.objects.first()
    tag = Tag(name="热门文章")
    tag.save()
    art.tag_set.add(tag)
    return HttpResponse('success')
