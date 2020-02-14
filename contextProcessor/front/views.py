from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from front.forms import RegisterForm, LoginForm
from front.models import User
from django.contrib import messages

# 内置的上下文处理器
# from django.template.context_processors import debug
# from django.template.context_processors import request
# from django.contrib.auth.context_processors import auth
# from django.contrib.messages.context_processors import messages
# from django.template.context_processors import media


def index(request):
    # user_id = request.session.get('user_id')
    # context = {}
    # try:
    #     user = User.objects.get(pk=user_id)
    #     context['front_user'] = user
    # except User.DoesNotExist:
    #     pass
    return render(request, 'index.html')


class SignView(View):

    def get(self, request):
        return render(request, 'sign.html')
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info(request, '用户或密码错误')
                # messages.add_message(request, messages.INFO, '用户或密码错误')
                return redirect(reverse('sign'))
        else:
            errors = form.get_error()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('sign'))
    

class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return redirect(reverse('register'))


def blog(request):
    return render(request, 'blog.html')