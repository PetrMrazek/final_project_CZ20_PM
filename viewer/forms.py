from django import forms
from viewer.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1, initial=1)


class OrderForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
