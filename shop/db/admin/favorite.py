from django.contrib import admin

from db.models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'product__name',)
    fields = ('user', 'product',)
    list_filter = ('user', 'product',)
    search_fields = ('user__username', 'product__name',)
