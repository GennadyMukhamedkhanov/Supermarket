from django.contrib import admin

from db.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_date', 'payment_method', 'transaction_id')
    fields = ('order',  'payment_method', 'transaction_id')
    list_filter = ('order',)
    search_fields = ('order',)
