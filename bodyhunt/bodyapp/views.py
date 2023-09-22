from typing import Any
from django.shortcuts import render, HttpResponse
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
    

class Cart(ListView):
    context_object_name = 'orditem'
    template_name = 'bodyapp/cart.html'
    
    def get_queryset(self):
        try:
            user = Customer.objects.get(session_anon=self.request.session['sesdata'])
            order = Order.objects.get(customer=user, complete=False)
            return order.orderitem_set.all()
        except Exception:
            return []
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = Customer.objects.get(session_anon=self.request.session['sesdata']) 
            order = Order.objects.get(customer=user, complete=False)
        except Exception:
            order = 0
        context['order'] = order
        return context
        # I could've used a mixins in order to follow the rule DRY. But, I assumed that it was going to take
        # more storage to create a "utils.py" then to write there a class with the methods, to import it and
        # then to specify as a parent class, so that's why i didn't follow this rule.
    

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
    
    if action == 'removeall':
        OrderItem.objects.all().delete()
        return JsonResponse('Succesfully removed all items!', safe=False)
    
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=Product.objects.get(id=productid))
    
    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1
    
    orderitem.save()
        
    if orderitem.quantity <= 0:
        orderitem.delete()
    elif action == 'removeitem':
        orderitem.delete()
    
    return JsonResponse('Succesfully adeed a product into the cart!', safe=False)


def notFound404(request, exception):
    return HttpResponse("<h1>The page wasn't found</h1>")