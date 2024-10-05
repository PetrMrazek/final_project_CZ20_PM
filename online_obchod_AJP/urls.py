"""
URL configuration for online_obchod_AJP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import HomePageView, ProductsView, ProductCreateView, ProductUpdateView, ProductDeleteView, UserView, \
    SingUpView
from viewer.models import Categorie, Product, Allergen
from django.contrib.auth.views import LoginView, LogoutView

admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Allergen)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='main'),
    path('products', ProductsView.as_view(), name='products'),
    path('products/add/', ProductCreateView.as_view(), name='add_product'),
    path('products/edit/<pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('products/delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('userpage/', UserView.as_view(), name='userpage'),
    path('accounts/register/', SingUpView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),

]

