# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm
from django.views.generic.base import TemplateView
from .forms import ProfileForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from . models import Profile

# @login_required
def home(request):
    context = {
        'login_form': LoginForm(),
        'signup_form': SignUpForm(),
        'user_form': SignUpForm(),
        'profile_form': ProfileForm(),
    }
    return render(request, 'accounts/register.html', context)


def signup(request):
    print "-" * 100
    if request.method == 'POST':
        if 'signup' in request.POST:
            print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuupppppppppppppp"
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            # Profile.objects.create(user=user)
            username = signup_form.cleaned_data.get('username')
            print username
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('stock:index')
            return redirect('accounts:profile')
            # return redirect('accounts:dashboard')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/register.html', {'signup_form': signup_form})


def view_profile(request):
    user = request.user
    profile = user.profile
    return render(request, "accounts/profile.html",
                  { 'user': user,
                    'profile': profile
                    })

from django.db import transaction
from django.shortcuts import get_object_or_404

@login_required
@transaction.atomic
def update_profile(request):
    print "update  profileee"
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        # signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)

        # if signup_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # signup_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('accounts:my_account')
        # else: pass
            # messages.error(request, _('Please correct the error below.'))
    else:
        # signup_form = SignUpForm(instance=request.user)
        # user =request.user
        # profile =user.profile
        profile_form = ProfileForm(instance=profile)
        print "GETTTTT PROFILE FORM"
        print request.method
        print profile_form
    return render(request, 'accounts/my_account.html', {
        'profile_form': profile_form
    })


def handler404(request):
    return render(request, 'core/404.html', status=404)


def handler500(request):
    return render(request, 'core/500.html', status=500)