from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:        
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        """first we call __init__ to set the form by default"""
        super().__init__(*args, **kwargs)

        """dictionary of placeholders that will show up in the form fields"""
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        """ 
        set the autofocus attribute on the full name field to true
        so the coursor will start in the full name field
        """
        self.fields['full_name'].widget.attrs['autofocus'] = True
        """
        Iterate throught he form fields adding a start to the placeholder
        if is required on the model
        """
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            """
            setting all the placeholder att to their values in the dictionary
            """
            self.fields[field].widget.attrs['placeholder'] = placeholder
            """CSS class"""
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            """
            removing the forms fields labels, we have placeholders set now
            """
            self.fields[field].label = False
