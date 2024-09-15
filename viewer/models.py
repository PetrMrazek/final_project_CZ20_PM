from django.db import models

# Create your models here.

class Product(models.Model):
    name = CharField(max_length=128)