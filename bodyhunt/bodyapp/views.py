from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.generic import ListView
from uuid import uuid4
import json


class MainShop(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 8
    template_name = 'bodyapp/main.html'


def updateCart(request):
    try:
        user = Customer.objects.get(session_anon=request.session['sesdata'])
    except Exception:
        request.session['sesdata'] = str(uuid4())
        user, created = Customer.objects.get_or_create(session_anon=request.session['sesdata'])
    
    order, created = Order.objects.get_or_create(customer=user, complete=False)
    data = json.loads(request.body)
    
    action = data['action']
    productid = data['productid']
    
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=Product.objects.get(id=productid))
    
    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1
    
    orderitem.save()
        
    if orderitem.quantity <= 0:
        orderitem.delete()
    
    return JsonResponse('Succesfully adeed a product into the cart!', safe=False)