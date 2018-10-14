# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm
from django.views.generic.base import TemplateView
# from .forms import LoginForm
from django.contrib.auth import views as auth_views


@login_required
def home1(request):
    return render(request, 'home.html')


def signup(request):
    print "-" * 100
    if request.method == 'POST':
        if 'signup' in request.POST:
            print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuupppppppppppppp"
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            print username
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('stock:index')
            # return redirect('accounts:dashboard')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/register.html', {'signup_form': signup_form})


# @login_required
def home(request):
    context = {
        'login_form': LoginForm(),
        'signup_form': SignUpForm()
    }
    return render(request, 'accounts/register.html', context)


# def login(request):
#     # ... logic for logging in ...
#     return render(request, 'accounts / register.html', auth_views.login)

''
# def signup(request):
#     # ... logic for signing up ...
#     return render(request, 'core/signup.html', context)