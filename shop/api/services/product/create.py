from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.services import Service
from rest_framework.exceptions import ParseError

from db.models import Product, Category


class ProductsCreateService(Service):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.IntegerField()
    image = forms.ImageField()
    stock = forms.IntegerField()

    def process(self):
        return self.creating_product

    @property
    def creating_product(self):
        try:
            product = Product.objects.create(
                name=self.cleaned_data['name'],
                description=self.cleaned_data['description'],
                price=self.cleaned_data['price'],
                category=self.get_category,
                image=self.cleaned_data['image'],
                stock=self.cleaned_data['stock']
            )

            return product

        except Exception as e:
            raise ParseError(f"Произошла ошибка: {str(e)}")
    @property
    def get_category(self):
        return get_object_or_404(Category, id=self.cleaned_data['category'])
