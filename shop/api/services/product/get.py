from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.services import Service

from db.models import Product


class GetProductService(Service):
    id = forms.IntegerField()

    def process(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])

