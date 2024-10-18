from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView, View, DetailView
from django.contrib.auth.forms import UserCreationForm

from online_obchod_AJP import settings
from viewer.forms import ProductForm, AddToCartForm, OrderForm, CateringContactForm
from viewer.models import Categorie, Product, Allergen, Order
from django.urls import reverse_lazy


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
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        context["product_detail"] = product
        context["product_allergens"] = product.allergens.all()
        return context

# Product Management for admin users
class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')
    permission_required = ('viewer.add_product',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Add Product'
        context['submit_button_text'] = 'Add Product'
        return context

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products')
    permission_required = ('viewer.change_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Edit Product'
        context['submit_button_text'] = 'Update Product'
        return context

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete_product.html'
    model = Product
    success_url = reverse_lazy('products')
    permission_required = 'viewer.delete_product'


# User management views
class SingUpView (CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('cart_summary')
class UserView(TemplateView):
    template_name = 'user.html'

# Cart management views
# View for adding items to the cart
class AddToCartView(FormView):
    form_class = AddToCartForm

    def form_valid(self, form):
        product_id = form.cleaned_data['product_id']
        quantity = form.cleaned_data['quantity']

        # Get or create the cart from the session
        cart = self.request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        # Save updated cart back to session
        self.request.session['cart'] = cart
        self.request.session.modified = True

        return redirect('cart_summary')


# View for displaying the cart summary
class CartSummaryView(TemplateView):
    template_name = 'cart_summary.html'

    def get_context_data(self, **kwargs):
        cart = self.request.session.get('cart', {})
        products = Product.objects.filter(id__in=cart.keys())

        # Create cart items with product, quantity, and total price
        cart_items = []
        for product in products:
            quantity = cart.get(str(product.id), 0)  # Ensure product.id is cast to string to match cart keys
            total_price = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': total_price
            })

        context = super().get_context_data(**kwargs)
        context['cart_items'] = cart_items
        return context


# View for updating cart items
class UpdateCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Validate product_id and quantity
        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except (ValueError, TypeError):
            return redirect('cart_summary')

        # Get the cart from the session
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            if quantity > 0:
                cart[str(product_id)] = quantity
            else:
                # If quantity is 0, remove the item from the cart
                del cart[str(product_id)]

        # Save updated cart back to session
        request.session['cart'] = cart
        request.session.modified = True

        return redirect('cart_summary')

# View for removing an item from the cart
class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')

        # Get the cart from the session
        cart = self.request.session.get('cart', {})

        # Remove the product if it exists in the cart
        if str(product_id) in cart:
            del cart[str(product_id)]

        # Save updated cart back to session
        self.request.session['cart'] = cart
        self.request.session.modified = True

        return redirect('cart_summary')

# Order Management Views

# View for placing an order
class PlaceOrderView(LoginRequiredMixin, FormView):
    template_name = 'place_order.html'
    form_class = OrderForm

    def form_valid(self, form):
        # Get user cart
        cart = self.request.session.get('cart', {})
        products = Product.objects.filter(id__in=cart.keys())

        # Calculate total price
        total_price = sum(product.price * cart[str(product.id)] for product in products)

        # Create the order
        order = Order.objects.create(
            user=self.request.user,
            items=cart,
            total_price=total_price,
            status='Pending',
        )

        # Clear the cart
        self.request.session['cart'] = {}
        self.request.session.modified = True

        return redirect('order_summary', pk=order.pk)

# View for reviewing an order
class OrderSummaryView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_summary.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()

        # Get the products and quantities from the order
        items = order.items
        products = Product.objects.filter(id__in=items.keys())

        # Create a list of products with their respective quantities
        order_items = []
        for product in products:
            quantity = items.get(str(product.id), 0)
            order_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity
            })

        context['order_items'] = order_items
        return context

class CateringContactView(FormView):
    template_name = 'catering.html'
    form_class = CateringContactForm
    success_url = reverse_lazy('catering_success')

    def form_valid(self, form):
        # Send email with form data
        subject = 'Catering Inquiry from {}'.format(form.cleaned_data['name'])
        message = (
            'Name: {name}\n'
            'Email: {email}\n'
            'Phone: {phone}\n'
            'Event Date: {event_date}\n'
            'Event Time: {event_time}\n'
            'Number of Guests: {guests}\n'
            'Estimated Budget: {budget}\n'
            'Comments: {comments}'
        ).format(**form.cleaned_data)

        send_mail(subject, message, settings.EMAIL_BACKEND, [settings.EMAIL_BACKEND])

        return super().form_valid(form)

class CateringSuccessView(TemplateView):
    template_name = 'catering_success.html'
