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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
