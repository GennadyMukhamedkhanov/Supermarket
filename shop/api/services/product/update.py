from rest_framework.generics import get_object_or_404
from service_objects.services import Service
from  django import forms

from db.models import Product


class UpdateProductService(Service):
    id = forms.IntegerField()
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)
    stock = forms.IntegerField(required=False)


    def process(self):
        return self.update_product()

    def update_product(self):
        product = self._get_product()
        product.name = self.cleaned_data.get('name') if self.cleaned_data.get('name') else product.name
        product.description = self.cleaned_data.get('description') if self.cleaned_data.get('description') else product.description
        product.price = self.cleaned_data.get('price') if self.cleaned_data.get('price') else product.price
        product.category = self.cleaned_data.get('category') if self.cleaned_data.get('category') else product.category
        product.image = self.cleaned_data.get('image') if self.cleaned_data.get('image') else product.image
        product.stock = self.cleaned_data.get('stock') if self.cleaned_data.get('stock') else product.stock
        product.save()

        return product


    def _get_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])

