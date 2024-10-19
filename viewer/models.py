from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.utils import timezone

# Create your models here.

# Categories of Products
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


# Customer Orders
class Order(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    items = models.JSONField(default=dict)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
