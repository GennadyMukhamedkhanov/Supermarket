from rest_framework import serializers

from db.models import Product, Category


class CategoryFromProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)

class ProductsListSerializer(serializers.ModelSerializer):
    category = CategoryFromProductSerializer()

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "image",
            "stock",
            "category"
        )
