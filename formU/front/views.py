from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import View
from front.forms import MessageBoardForm


class IndexView(View):

    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print(title, content, email, reply)
            return HttpResponse('成功')
        else:
            print(form.errors)
            return HttpResponse('失败')