from django.urls import path
from .views import *


urlpatterns = [
    path('', MainShop.as_view(), name='main'),
]