from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', MainShop.as_view(), name='main'),
    path('updatecart/', updateCart, name='updatecart'),
    path('cart', Cart.as_view(), name='cart'),
]