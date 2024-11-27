from django.shortcuts import render, HttpResponse, redirect
from .models import Media
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')

@login_required
def home(request):
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies.html')

def tvshows(request):
    return render(request, 'tvshows.html')

def prime(request):
    return render(request, 'prime.html')

def sub(request):
    return render(request, 'sub.html')

def play(request):
    if request.method == "POST":
        return redirect('video')
    return render(request, 'play.html')

def video(request):
    media_items = Media.objects.filter(title="Upload Series")
    return render(request, 'video.html', {'media_items': media_items})

def pushpa(request):
    if request.method == "POST":
        return redirect('pushpaV')
    return render(request, 'pushpa.html')

def pushpa_v(request):
    media_items = Media.objects.filter(title="Pushpa: The Rise (Telugu)")
    return render(request, 'pushpa-video.html', {'media_items': media_items})

