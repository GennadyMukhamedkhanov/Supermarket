from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from django import forms

from db.models import Product, User, CartItem


class DeleteProductsInCartService(Service):
    id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self.delete_obj()
        return True

    def delete_obj(self):
        product = self.get_product()
        cart = self.cleaned_data['user'].cart
        obj = get_object_or_404(CartItem, cart=cart, product=product)
        obj.delete()


        return True

    def get_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])
