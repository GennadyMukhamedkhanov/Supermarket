from rest_framework import serializers

from db.models import Category, Favorite


class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    product = serializers.CharField(source='product.name')

    class Meta:
        model = Favorite
        fields = ('user', 'product')
