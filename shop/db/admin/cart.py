from django.contrib import admin

from db.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at',)
    fields = ('user',)
    list_filter = ('user__username',)
    search_fields = ('user',)

