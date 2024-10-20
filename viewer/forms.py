from datetime import date
import re
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

    SHIPPING_CHOICES = [
        ('pickup', 'Pick up (free)'),
        ('standard', 'Standard shipping around Prague (79 CZK)'),
    ]
    shipping_option = forms.ChoiceField(choices=SHIPPING_CHOICES, widget=forms.RadioSelect)

class CateringContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    event_date = forms.DateField(required=False)
    event_time = forms.TimeField(required=False)
    guests = forms.IntegerField(min_value=1, required=False)
    budget = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        # Required format: +[country code] followed by nine digits
        pattern = r'^\+\d{1,3}\s?\d{3}\s?\d{3}\s?\d{3}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                'Invalid phone number format. It should start with a country code followed by nine digits (e.g. +420 737 242 659).'
            )

        return phone
    def clean(self):
        cleaned_data = super().clean()

        event_date = cleaned_data.get('event_date')
        event_time = cleaned_data.get('event_time')

        if event_date or event_time:
            if not event_date:
                self.add_error('event_date', 'Event date is required if event time is provided')
            if not event_time:
                self.add_error('event_time', 'Event time is required if event date is provided')
        if event_date and event_date < date.today():
            self.add_error('event_date', 'Event date cannot be in the past')

        return cleaned_data

class PriceFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, label='Min Price', min_value=0)
    max_price = forms.IntegerField(required=False, label='Max Price', min_value=0)