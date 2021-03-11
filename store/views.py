from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Store.html', context)


def kart(request):
    return render(request, 'Kart.html')


def checkout(request):
    return render(request, 'Checkout.html')


def login(request):
    return render(request, 'Login.html', {'name': 'eKart'})
