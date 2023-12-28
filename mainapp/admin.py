from django.contrib import admin
from mainapp.models import Product,Brand,Size,Color,BasketItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')  
    list_filter = ('name','brand')  
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)

admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(BasketItem)