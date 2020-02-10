from django.urls import re_path, path
from article import views


urlpatterns = [
    path('', views.article),
    # re_path('list/(?P<categories>\w+|(\w+\+\w+)+)', views.article_list),
    path('list/<cate:categories>/', views.article_list)
]
