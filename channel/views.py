from django.shortcuts import render

# Create your views here.
def top_videos(request):
    return render(request, 'top_videos.html')
