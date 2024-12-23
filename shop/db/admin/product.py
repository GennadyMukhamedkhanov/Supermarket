from django.contrib import admin

from db.models import OrderItem
from db.models.product import Product


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image', 'stock',)
    fields = ('name', 'description', 'price', 'category', 'image', 'stock',)
    list_filter = ('name',)
    search_fields = ('name', 'description', 'category__name')

    inlines = [OrderItemInline]