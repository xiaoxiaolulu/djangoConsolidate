from django.shortcuts import render


def index(request):
    context = {
        'info': "<a href='www.baidu.com'>百度<a/>"
    }
    return render(request, 'index.html', context=context)
