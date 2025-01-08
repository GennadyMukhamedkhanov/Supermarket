from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.services import Service

from db.models import Product, Category


class GetProductByCategoryService(Service):
    category_id = forms.IntegerField()

    def process(self):
        return self.get_products_by_category()


    def get_category(self):
        return get_object_or_404(Category, id=self.cleaned_data['category_id'])

    def get_products_by_category(self):
        category = self.get_category()
        return category.products.all()

