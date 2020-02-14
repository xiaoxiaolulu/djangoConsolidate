from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from front.forms import RegisterForm, LoginForm
from front.models import User


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
                return redirect(reverse('sign'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
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