from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
