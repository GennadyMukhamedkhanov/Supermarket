from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service

from db.models import User, Cart, CartItem, Product


class AddProductInCartService(Service):
    id = forms.IntegerField()
    amount_goods = forms.IntegerField()
    user = ModelField(User)

    def process(self):

        id_cart = self.get_id_cart()
        self.add_product_in_cart(id_cart)
        return True

    def get_id_cart(self):
        user = self.cleaned_data['user']
        cart, created = Cart.objects.get_or_create(user=user)
        return cart.id

    def add_product_in_cart(self, id_cart):
        obj = CartItem.objects.get_or_create(cart_id=id_cart, product_id=self.cleaned_data['id'])[0]
        obj.quantity += self.validation_amount_goods()
        obj.save()

    def validation_amount_goods(self):
        product = get_object_or_404(Product, id=self.cleaned_data['id'])
        stock = product.stock

        if self.cleaned_data['amount_goods'] > stock:
            return stock

        else:
            return self.cleaned_data['amount_goods']
