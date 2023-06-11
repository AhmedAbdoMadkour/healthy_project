from django.shortcuts import render
from blog.models import Article
from .models import Testimonials
# Create your views here.
def home(request):
    articles = Article.objects.prefetch_related('comments').all()
    testimonials = Testimonials.objects.all()
    return render(request, "index.html", {"articles": list(articles), "testimonials":list(testimonials)})
