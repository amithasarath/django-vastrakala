# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True,null=True,upload_to='profile-images/')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house_no = models.TextField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    landmark = models.CharField(max_length=30, blank=True)
    district = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    pincode = models.IntegerField(blank=True)
    mobile_number = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)