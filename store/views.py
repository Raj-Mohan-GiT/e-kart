from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'Store.html')


def kart(request):
    return render(request, 'Kart.html')


def checkout(request):
    return render(request, 'Checkout.html')


def login(request):
    return render(request, 'Login.html', {'name': 'eKart'})
