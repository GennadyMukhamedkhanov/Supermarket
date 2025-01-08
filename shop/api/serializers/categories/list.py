from rest_framework import serializers

from db.models import  Category


class ListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'