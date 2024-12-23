from django.contrib import admin

from db.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'created_at',
                    'total_price', 'is_paid', 'payment_method',)
    fields = ('user', 'total_price', 'is_paid', 'payment_method',)
    list_filter = ('user__username',)
    search_fields = ('user__username',)

    inlines = [OrderItemInline]
