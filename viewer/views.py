from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from viewer.forms import ProductForm
from viewer.models import Categorie, Product
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    }
class ProductsView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = Categorie.objects.all()

        category_products = {}
        for category in all_categories:
            category_products[category] = Product.objects.filter(category=category)

        context['category_products'] = category_products
        return context

class ProductCreateView(CreateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')

class ProductUpdateView(UpdateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')

class ProductDeleteView(DeleteView):
    template_name = 'confirm_delete_product.html'
    model = Product
    success_url = reverse_lazy('products')

