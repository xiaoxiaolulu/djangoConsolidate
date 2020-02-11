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

    # 会使用大小写敏感
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content` FROM `front_article`
    # WHERE `front_article`.`title` LIKE BINARY %zh9ngs%
    article2 = Article.objects.filter(title__contains='zh9ngs')
    print(article2.query)

    # 忽略大小写
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content` FROM `front_article`
    # WHERE `front_article`.`title` LIKE %zh9ngs%
    article3 = Article.objects.filter(title__icontains='zh9ngs')
    print(article3.query)
    return HttpResponse("success")
