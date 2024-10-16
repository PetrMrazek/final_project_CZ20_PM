from viewer.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key! Create one!
        if not cart:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)  # Store the product ID as a string
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity
            }
        # Debugging output
        print("Cart session data:", self.cart)
        print("Cart contents after adding:", self.cart)

        self.session.modified = True

    def __len__(self):
        return sum(item.get('quantity', 1) for item in self.cart.values())

    def get_prods(self):
        # Get product IDs from cart (keys are strings)
        product_ids = list(self.cart.keys())

        # Use these IDs to look up products in the database
        products = Product.objects.filter(id__in=product_ids)

        # Return the queried products
        return products
