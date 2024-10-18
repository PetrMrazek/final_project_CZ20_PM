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

class CateringContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    event_date = forms.DateField()
    event_time = forms.TimeField()
    guests = forms.IntegerField(min_value=1)
    budget = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)