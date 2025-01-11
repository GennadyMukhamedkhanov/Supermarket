from rest_framework import serializers

from db.models import CartItem


class ListProductsInCartSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity'
        )
