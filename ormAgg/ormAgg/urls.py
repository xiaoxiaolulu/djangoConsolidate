"""ormAgg URL Configuration

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

from front import views

urlpatterns = [
    path('', views.index),
    path('a/', views.index02),
    path('b/', views.index03),
    path('c/', views.index04),
    path('d/', views.index05),
    path('e/', views.index06),
    path('f/', views.index07),
    path('g/', views.index08),
    path('z/', views.index09),
    path('m/', views.index10),
    path('l/', views.index11),
    path('aa/', views.index12),
    path('bb/', views.index13),
    path('cc/', views.index14),
    path('dd/', views.index15)
]

