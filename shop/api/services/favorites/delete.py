from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from django import forms

from db.models import Category, User, Product, Favorite


class DeleteProductsInFavoritesService(Service):
    product_id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self.delete_product_in_favorites()
        return True

    def get_obj_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['product_id'])

    def delete_product_in_favorites(self):
        favorite = get_object_or_404(Favorite, user=self.cleaned_data.get('user'), product=self.get_obj_product())
        favorite.delete()
        return True
