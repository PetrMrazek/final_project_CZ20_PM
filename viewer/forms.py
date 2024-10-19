from django import forms
from viewer.models import Product

from django.core.exceptions import ValidationError

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

    def clean(self):
        super(CateringContactForm, self).clean()
        if self.cleaned_data.get('name') != self.cleaned_data.get('name').capitalize():
            raise ValidationError("Name must start with capital letter")
        return self.cleaned_data

class PriceFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, label='Min Price', min_value=0)
    max_price = forms.IntegerField(required=False, label='Max Price', min_value=0)