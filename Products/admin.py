from django.contrib import admin
from .models import Products, Producent, Category

# Register your models here.

admin.site.register(Products)
admin.site.register(Producent)
admin.site.register(Category)