from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from viewer.forms import ProductForm
from viewer.models import Categorie, Product, Allergen
from viewer.cart import Cart
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages


# Homepage set up
class HomePageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    }

# Product list filter by category
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

# Product Details
class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context["product_detail"] = Product.objects.get(pk=self.kwargs['pk'])
        context["product_allergens"] = Allergen.objects.get(pk=self.kwargs['pk'])
        return context

# Product Management for admin users
class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')
    permission_required = ('viewer.add_product',)

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')
    permission_required = ('viewer.change_product')

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete_product.html'
    model = Product
    success_url = reverse_lazy('products')
    permission_required = 'viewer.delete_product'



# User management views
class SingUpView (CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
class UserView(TemplateView):
    template_name = 'user.html'

# Order management views
def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	#quantities = cart.get_quants
	#totals = cart.cart_total()
	return render(request, "cart_summary.html", {"cart_products":cart_products})


def cart_add(request):
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get product
        product_id = int(request.POST.get('product_id'))

        # lookup for product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return response
        response = JsonResponse({'qty': cart_quantity})
        return response





