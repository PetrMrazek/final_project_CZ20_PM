from django.db import models
from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)

# Create your models here.

class Product(models.Model):
    name = CharField(max_length=128)
    weight = IntegerField()
