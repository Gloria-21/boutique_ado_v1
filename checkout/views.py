from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """bag from the session"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    """Order Form"""
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KqlEyGQ9tfLIql4vUUDUJ2yKDiWDHQ358jRFiHXP4yLdBr2QIlOWtgOouq33KqwpnPD9wF6k5g1MQmAzqWhOGzc00md5S5KLv',
        'client_secret': 'test client secret', 
    }

    return render(request, template, context)