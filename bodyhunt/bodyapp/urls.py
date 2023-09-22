from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60 * 10)(MainShop.as_view()), name='main'),
    path('updatecart/', updateCart, name='updatecart'),
    path('cart', Cart.as_view(), name='cart'),
]