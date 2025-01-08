from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.services import Service

from db.models import Product


class DeleteProductService(Service):
    id = forms.IntegerField()

    def process(self):
        self.delete_product()
        return True

    def delete_product(self):
        product = get_object_or_404(Product, id=self.cleaned_data['id'])
        product.delete()


