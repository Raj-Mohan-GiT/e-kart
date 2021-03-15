from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .models import *

# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Store.html', context)


def kart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_kart_total': 0,
                 'get_total_count': 0,
                 'shipping': False}

    context = {'items': items,
               'order': order}

    return render(request, 'Kart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_kart_total': 0,
                 'get_total_count': 0}

    context = {'items': items,
               'order': order,
               'shipping': False}

    return render(request, 'Checkout.html', context)


def login(request):
    return render(request, 'Login.html', {'name': 'eKart'})


def update_item(request):
    data = json.loads(request.body)
    product_id = data['Product_id']
    action = data['Action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    order_item, created = OrderItem.objects.get_or_create(product=product, order=order)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity < 1:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)