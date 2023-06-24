from django.urls import path
from . import views

# app_name = "blog"
urlpatterns = [
    path('articles/', views.articles, name='blog'),
    path('article/<int:pk>', views.article_details, name='article'),

]
