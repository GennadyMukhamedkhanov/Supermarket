from django.contrib import admin

from db.models import User, Order


class OrderInline(admin.StackedInline):
    model = Order
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_manager', 'is_admin')
    fields = ('username', 'phone_number', 'is_manager',
              'is_admin', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'phone_number', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'phone_number', 'first_name', 'last_name', 'email')
    inlines = [OrderInline]
