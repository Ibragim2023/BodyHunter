from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, unique=True)
    session_anon = models.CharField(max_length=120, null=True, blank=True, editable=False)
    
    def __str__(self):
        return 'UsersAnon'
    
    class Meta:
        verbose_name = 'ПользовательЭкземпляр'
        verbose_name_plural = 'ПользовательЭкземпляры'
        

class Product(models.Model):
    name = models.CharField(max_length=23, null=True, unique=True)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True)    
    added = models.DateTimeField(auto_now_add=True, null=True)
    
    @property
    def generalprice(self):
        total = 0
        orditems = self.orderitem_set.all()
        for i in orditems:
            total += i.countorditem
        return total
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    
class OrderItem(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    
    @property
    def countorditem(self):
        return self.product.price * self.quantity
    
    class Meta:
        verbose_name = 'Товар заказа'
        verbose_name_plural = 'Товары заказов'
    

class Shipping(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=120, null=True)
    street = models.CharField(max_length=150, null=True)
    homenumber = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.street + str(self.homenumber)
    
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'