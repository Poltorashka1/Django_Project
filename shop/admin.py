from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models


# Register your models here.

class ShopModelAdmin(ModelAdmin):
    model = models.Shop
    list_display = ('name', 'price',)
    list_display_links = ('name',)


admin.site.register(models.Shop, ShopModelAdmin)
