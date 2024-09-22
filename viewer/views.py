from django.views.generic import TemplateView
from viewer.models import Categorie, Product

class HomePageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    }

class ProductsView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all categories
        all_categories = Categorie.objects.all()

        # Create a dictionary to hold categories and their respective products
        category_products = {}

        # For each category, get the related products
        for category in all_categories:
            category_products[category] = Product.objects.filter(category=category)

        # Pass the data to the context
        context['category_products'] = category_products
        return context