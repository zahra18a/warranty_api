from django.contrib import admin

from warranties.models import Warranty,Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_code')
    search_fields = ('name', 'product_code')
    ordering = ('id',)

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'warranty_code', 'customer_name', 'created_at')
    search_fields = ('warranty_code', 'customer_name')
    list_filter = ('created_at', 'product')
    ordering = ('-created_at',)
