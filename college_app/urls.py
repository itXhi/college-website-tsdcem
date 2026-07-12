from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_home, name='home'),
    path('home/', views.website_home, name='home'),
]