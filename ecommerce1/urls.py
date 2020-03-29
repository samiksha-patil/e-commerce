"""
ecommerce1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from shop import views as shop_views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
     path('',user_views.home,name='main'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html') ,name='logout'),
    path('item/',shop_views.item_list,name='item_list'),
    path('products/<slug>', shop_views.ItemDetailView.as_view(template_name='product.html'),name='product'),
    path('add_to_cart/<slug>/',shop_views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<slug>/',shop_views.remove_from_cart,name='remove_from_cart'),
    path('order-summary/',shop_views.OrderSummaryView.as_view(),name='order-summary'),
    path('remove_item_from_cart/<slug>/',shop_views.remove_single_item_from_cart,name='remove_single_item_from_cart'),
    path('checkout/',shop_views.CheckoutView.as_view(),name='checkout'),
    path('payment/<payment_option>/',shop_views.PaymentView.as_view(),name='payment'),
]
