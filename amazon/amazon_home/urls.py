from django.urls import path
from . import views
urlpatterns = [
    path("home", views.method),
    path("home2", views.method2),
    path("home3", views.method3),
    path("home4", views.method4),
    ]
