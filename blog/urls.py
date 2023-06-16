from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='blog'),
    path('article/<int:id>', views.article_details, name='article'),

]
