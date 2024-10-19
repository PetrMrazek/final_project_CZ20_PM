from django.contrib import admin
from viewer.models import Categorie, Product, Allergen, Order
# Register your models here.
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Allergen)
admin.site.register(Order)
