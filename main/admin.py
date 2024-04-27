from django.contrib import admin

from .models import Product, Profile, ProductImage, Comment, Rating

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Comment)
admin.site.register(Rating)