from django.contrib import admin

from db.models import Category, Product


class Productline(admin.StackedInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    fields = ('name', 'slug')
    list_filter = ('name', 'slug',)
    search_fields = ('name', 'slug',)
    inlines = [Productline, ]
