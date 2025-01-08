from rest_framework import serializers

from db.models import Product


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'