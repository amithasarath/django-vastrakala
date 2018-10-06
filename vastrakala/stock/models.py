# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ItemType(models.Model):
    type = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('type',)

    def __str__(self):
        return self.type


class ItemGroup(models.Model):
    group = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    group_image = models.ImageField(blank=True,null=True,upload_to='group/')
    price = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    description = models.TextField(max_length=200,blank=True,help_text="optional")
    available =models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('group',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.group


class ItemStock(models.Model):
    item_name = models.CharField(max_length=50)
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, db_index=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    item_image = models.ImageField(blank=True,null=True,upload_to='items/')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=200,null=True, blank=True, help_text="optional")
    available = models.BooleanField(default=0)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('item_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.item_name