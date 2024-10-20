from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from viewer.models import Product, Categorie, Order
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

# Create your tests here.

class ProductsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categorie.objects.create(name="Test Category")
        Product.objects.create(title="Test Product", description="Description", category=self.category, price=100)

    def test_products_view_status_code(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products_view_context_data(self):
        response = self.client.get(reverse('products'))
        self.assertTrue('category_products' in response.context)
        self.assertEqual(len(response.context['category_products'][self.category]), 1)

class ProductCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(username='admin', password='admin123', email='admin@example.com')

    def test_product_create_view_requires_login(self):
        # Ensure the product creation page is restricted to unauthorized users
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Log in as admin
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a category and product for testing
        self.category = Categorie.objects.create(name="Cookies")
        self.product = Product.objects.create(title="Test Chocolate cookie", description="A delicious cookie", category=self.category, price=59)

    def test_product_creation(self):
        # Test that a product can be created and accessed
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(self.product.title, "Test Chocolate cookie")

    def test_category_relationship(self):
        # Test that the product is linked to the correct category
        self.assertEqual(self.product.category.name, "Cookies")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='userpassword')
        self.order = Order.objects.create(user=self.user, items={"1": 2}, total_price=50.00, created_at=timezone.now())

    def test_order_creation(self):
        # Test that an order can be created
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.order.total_price, 50.00)

    def test_order_user_relationship(self):
        # Test that the order is linked to the correct user
        self.assertEqual(self.order.user.username, 'user1')


class ProductSearchSeleniumTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)
        cls.category = Categorie.objects.create(name="Baked Goods")
        Product.objects.create(title="Chocolate Cake", description="Delicious chocolate cake", category=cls.category, price=200)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_product_search(self):
        self.selenium.get(f'{self.live_server_url}/products')

        search_box = self.selenium.find_element(By.NAME, "q")
        search_box.send_keys('Chocolate Cake')

        self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.assertIn("Chocolate Cake", self.selenium.page_source)



