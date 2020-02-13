"""mehodDecorator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add/', views.add),
    path('home/', views.home, name='index'),
    path('signup/', views.signup, name='signup'),
    path('a/', views.index02),
    path('f/', views.csv),
    path('ff/', views.csv_template),
    path('fff/', views.large_csv),
    path('book/', views.BookListView.as_view(), name='book'),
    path('add_book/', views.AddBookViews.as_view(), name='add'),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('abab/', views.AboutView.as_view()),
    path('add_article/', views.add_article),
    path('list/', views.ArticleListView.as_view())
]
