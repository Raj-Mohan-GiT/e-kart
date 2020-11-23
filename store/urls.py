from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('kart/', views.kart, name='kart'),
    path('checkout/', views.checkout, name='checkout')
]
