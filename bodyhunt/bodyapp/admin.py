from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Shipping)
admin.site.register(Order)
admin.site.register(OrderItem)