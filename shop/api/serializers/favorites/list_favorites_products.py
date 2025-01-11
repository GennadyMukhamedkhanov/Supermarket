from rest_framework import serializers

from db.models import Category, Favorite


class FavoritesProductsSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = Favorite
        fields = ('product',)
