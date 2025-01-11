from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from django import forms

from db.models import Product, User, CartItem


class UpdateAmountGoodsInCartProductsService(Service):
    id = forms.IntegerField()
    user = ModelField(User)
    amount_goods = forms.CharField()

    def process(self):
        return self._update_amount_good

    @property
    def _update_amount_good(self):
        product = self.get_product()
        cart = self.cleaned_data['user'].cart
        obj = get_object_or_404(CartItem, cart=cart, product=product)
        obj.quantity = self.cleaned_data.get('amount_goods')
        obj.save()

        return obj

    def get_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])
