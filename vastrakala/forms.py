from django import forms
from . models import Dealer,Reseller,Customer,SalesOrder
from django.utils.translation import gettext_lazy as _


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'

class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'
        # fields = ['reseller','customer','dealer_code','cost_price','selling_price','order_status']
        # exclude = ['title']
        # widgets = {
        #     'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        widgets ={
            'client_type': forms.Select(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'order_status': forms.Select(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'reseller': forms.Select(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'customer': forms.Select(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'type': forms.Select(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'qty': forms.NumberInput(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'booking_date': forms.DateInput(attrs={
                'style': 'border-color: green;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            })
        }
        labels = {
            'order_status': _('Status of Order'),
        }
        help_texts = {
            'dealer_code': _('Short code of the Dealer.'),
            'client_type': _('Type of the client.'),
            'reseller': _('Name of Reseller.'),
        }
        error_messages = {
            'dealer_code': {
                'max_length': _("This code's name is too long."),
            },
        }
