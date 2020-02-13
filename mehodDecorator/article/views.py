
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from article.models import Article
from django.views.decorators.http import require_http_methods, require_GET


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
    return HttpResponse("sign")