from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('tvshows/', views.tvshows, name='tvshows'),
    path('prime/', views.prime, name='prime'),
    path('addons/', views.sub, name='sub'),
    path('play/', views.play, name = "play"),
    path('video/', views.video, name = "video"),
    path('pushpa/', views.pushpa, name = "pushpa"),
    path('pushpaV/', views.pushpa_v, name = "pushpaV")

]
