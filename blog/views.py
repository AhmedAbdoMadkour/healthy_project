from django.shortcuts import render
from .models import Article
# Create your views here.
def articles(request):
    articles = Article.objects.prefetch_related('comments').prefetch_related('likes').all()
    return render(request, 'blog.html', {"articles": list(articles), "user": request.user})
