from django import forms
from . models import Dealer,Reseller,Customer,SalesOrder
from django.utils.translation import gettext_lazy as _


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
        widgets = {
            'dealer_code': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder' : "Enter Dealer Code"
            }),
            'dealer_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Enter Dealer Name"
            })
        }

class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = '__all__'
        widgets = {
            'reseller_name': forms.TextInput(attrs={
                'class': "form-control"
            })
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': "form-control"
            })
        }


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'
        # appointment_date = forms.DateField(
        #     widget=forms.DateInput(format='%m/%d/%Y'),
        #     input_formats=('%m/%d/%Y',)
        # )
        # fields = ['reseller','customer','dealer_code','cost_price','selling_price','order_status']
        # exclude = ['title']
        # widgets = {
        #     'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        widgets ={
            'client_type': forms.Select(attrs={
                'style': 'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'order_status': forms.Select(attrs={
                'style': 'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class': "form-control"
            }),
            'reseller': forms.Select(attrs={
                'style':  'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'customer': forms.Select(attrs={
                'style':  'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'type': forms.Select(attrs={
                'style':  'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'qty': forms.NumberInput(attrs={
                'style':  'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'booking_date': forms.DateInput(format='%d-%m-%Y',attrs={
                'style':  'margin-bottom: 15px;',
                'input_formats' : "%d-%m-%Y",
                'type':'date',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'cost_price': forms.NumberInput(attrs={
                'style':  'margin-bottom: 15px;',
                'step' : 1,
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'selling_price': forms.NumberInput(attrs={
                'style':  'margin-bottom: 15px;',
                'step': 1,
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'dealer': forms.Select(attrs={
                'style':  'margin-bottom: 15px;',
                # 'placeholder': 'Write your name here'
                'class':"form-control"
            }),
            'tracking_id': forms.TextInput(attrs={
                'style':  'margin-bottom: 15px;',
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
