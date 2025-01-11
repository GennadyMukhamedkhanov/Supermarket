from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from django import forms

from db.models import Category, User, Product, Favorite


class AddProductsInFavoritesService(Service):
    product_id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        return self.add_product_in_favorites()[0]

    def get_obj_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['product_id'])

    def add_product_in_favorites(self):
        return Favorite.objects.get_or_create(user=self.cleaned_data.get('user'), product=self.get_obj_product())
