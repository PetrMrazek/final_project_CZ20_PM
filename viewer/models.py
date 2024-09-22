from django.db import models
from django.db.models import (CharField, DateField, DateTimeField, ForeignKey, IntegerField, TextField, ImageField,
                              DecimalField)

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=255)


class Allergen(models.Model):
    name = models.CharField(max_length=255)
    allergen_number = models.IntegerField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    allergens = models.ManyToManyField(Allergen)
