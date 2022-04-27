from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    # we take the order number as an argument and change view and name to checkout_success
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]