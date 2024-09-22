from django.views.generic import TemplateView
from viewer.models import Categorie

class HomePageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    }

class ProductsView(TemplateView):
    template_name = 'products.html'
    extra_context = {
        'all_categories': Categorie.objects.all()
    }