from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Article, Category


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

    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content` FROM `front_article`
    # WHERE `front_article`.`id` IN (1, 2)
    article4 = Article.objects.filter(id__in=[1, 2])
    print(article4.query)

    # 通过文章分类查找文章
    # SELECT `front_category`.`id`, `front_category`.`name` FROM `front_category` INNER JOIN `front_article` ON
    # (`front_category`.`id` = `front_article`.`category_id`) WHERE `front_article`.`id` IN (1, 2)
    category = Category.objects.filter(article__id__in=[1, 2])
    print(category.query)
    return HttpResponse("success")


def index02(request):

    # 大于
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`id` > 2
    art = Article.objects.filter(id__gt=2)
    print(art.query)

    # 大于等于
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`id` >= 2
    art1 = Article.objects.filter(id__gte=2)
    print(art1.query)

    # 小于
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`id` < 2
    art2 = Article.objects.filter(id__lt=2)
    print(art2.query)

    # 小于等于
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`id` <= 2
    art3 = Article.objects.filter(id__lte=2)
    print(art3.query)
    return HttpResponse('success')


def index03(request):
    # 首字母为xxx
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`title` LIKE BINARY 干%
    art = Article.objects.filter(title__startswith='干')
    print(art.query)

    # 忽略大小写
    # SELECT `front_article`.`id`, `front_article`.`title`, `front_article`.`content`, `front_article`.`category_id`
    # FROM `front_article` WHERE `front_article`.`title` LIKE 干%
    art1 = Article.objects.filter(title__istartswith='干')
    print(art1.query)

    # title__iendswith 忽略大小写
    # title__endswith 以xxx结束
    return HttpResponse('success')
