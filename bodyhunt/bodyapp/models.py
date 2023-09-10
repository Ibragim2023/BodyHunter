from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, null=True, db_index=True)
    slug = models.SlugField(unique=True, null=True, db_index=True)
    

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=30)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    

class Order(models.Model):
    complete = models.BooleanField(default=False, null=True)    
    added = models.DateTimeField(auto_now_add=True, null=True)
    
    @property
    def generalprice(self):
        total = 0
        orditems = self.orderitem_set.all()
        for i in orditems:
            total += i.countorditem
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    
    @property
    def countorditem(self):
        return self.product.price * self.quantity
    

class Shipping(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=120, null=True)
    street = models.CharField(max_length=150, null=True)
    homenumber = models.IntegerField(null=True, blank=True)