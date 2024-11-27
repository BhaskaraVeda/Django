from django.urls import path
from .views import register,signin
urlpatterns = [
    path('1', register,name='register'),
    path('',signin,name='signin'),
]
