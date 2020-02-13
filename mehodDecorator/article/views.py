import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from article.models import Article
from django.views.decorators.http import require_http_methods, require_GET
from django.core.handlers.wsgi import WSGIRequest
from django.template import loader


# @require_http_methods(['GET'])
@require_GET
def index(request):

    article = Article.objects.all()
    return render(request, 'index.html', context={'articles': article})


@require_http_methods(['POST'])
def add(request):
    t = request.POST.get('title')
    c = request.POST.get('content')
    Article.objects.create(title=t, content=c)
    return HttpResponse("success")


def home(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("home")
    else:
        return redirect(reverse('signup'))


def signup(request):
    print(request)
    return HttpResponse("sign")


def index02(request):
    person = {
        "name": "hahah"
    }
    # p_str = json.dumps(person)
    # return HttpResponse(p_str, content_type='application/json')
    return JsonResponse(person)


def csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv"
    writer = csv.writer(response)
    writer.writerow(['user', 'age'])
    writer.writerow(['hahah', 18])
    return response


def csv_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv"
    content = {
        "rows": [
            ['username', 'age'],
            ['sahssda', 18]
        ]
    }
    template = loader.get_template('abc.txt')
    csv_template = template.render(content)
    response.content = csv_template
    return response
