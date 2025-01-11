from django.shortcuts import get_list_or_404
from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from django import forms

from db.models import Category, User, Product, Favorite


class ListFavoritesProductService(Service):
    user = ModelField(User)

    def process(self):
        return self._get_list_favorites

    @property
    def _get_list_favorites(self):
        return get_list_or_404(Favorite, user=self.cleaned_data['user'])
