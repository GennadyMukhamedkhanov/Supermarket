from django.shortcuts import get_list_or_404
from service_objects.fields import ModelField
from service_objects.services import Service

from db.models import User, CartItem


class ListProductsInCartService(Service):
    user = ModelField(User)

    def process(self):
        return self._get_list_products_in_cart

    @property
    def _get_list_products_in_cart(self):
        return get_list_or_404(CartItem, cart__user=self.cleaned_data['user'])
