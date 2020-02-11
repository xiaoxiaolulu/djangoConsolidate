from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Article


def index(request):
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`
    # FROM `front_article` WHERE `front_article`.`id` = 1
    article = Article.objects.filter(id__exact=1)
    print(article.query)
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`
    # FROM `front_article` WHERE `front_article`.`id` LIKE 1
    article1 = Article.objects.filter(id__iexact=1)
    print(article1.query)
    return HttpResponse("success")
