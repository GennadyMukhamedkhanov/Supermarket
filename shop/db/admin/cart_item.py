from django.contrib import admin

from db.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)
    fields = ('cart', 'product', 'quantity',)
    list_filter = ('product__name', 'cart__user__username',)
    search_fields = ('product__name', 'cart__user__username',)
