import datetime

from django.db import models
from django.db.models import (CharField, DateField, DateTimeField, ForeignKey, IntegerField, TextField, ImageField,
                              DecimalField, EmailField)

# Create your models here.
# Categories od Products
class Categorie(models.Model):
    name = models.CharField(max_length=255)

# Allergens of Products
class Allergen(models.Model):
    name = models.CharField(max_length=255)
    allergen_number = models.IntegerField()

# Products
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    allergens = models.ManyToManyField(Allergen)

# Customers
class Customer(models.Model):
    user_login = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

# Orders
class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)
    date_of_submission = models.DateField(default=datetime.datetime.today)
    order_lines = models.ForeignKey(OrderLine, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

