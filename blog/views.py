from django.shortcuts import render 
from .models import Article
# Create your views here.


def articles(request):
    articles = Article.objects.prefetch_related('comments').prefetch_related('likes').all()
    return render(request, 'blog.html', {"articles": list(articles), "user": request.user})


def article_details(request, pk):
    # if request.method == "POST":
    # else:
    article = Article.objects.prefetch_related('comments').get(pk=pk)
    recent_articles = Article.objects.all().order_by('-publish_date')[:3]
    return render(request, "read_article.html", {"article": article, "recent_articles": recent_articles})
