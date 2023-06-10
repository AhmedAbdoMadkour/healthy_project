from django.shortcuts import render

# Create your views here.
def plans(request):
    return render(request, 'pricing.html')