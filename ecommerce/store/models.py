from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField( max_length=120, null=True)
    email = models.CharField( max_length=120, null=True)
    
    def __str__(self):
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=120, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    # TODO: image field
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now=False, auto_now_add=False)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default = 0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=False)
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.address
    
