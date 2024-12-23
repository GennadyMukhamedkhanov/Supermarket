from django.contrib import admin

from db.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    fields = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product', )
    search_fields = ('order', 'product', )


