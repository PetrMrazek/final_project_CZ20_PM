from django.views.generic import TemplateView
from viewer.models import Product

class HomePageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
        'all_products': Product.objects.all(),

    }

