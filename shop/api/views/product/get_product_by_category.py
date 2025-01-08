from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.product.list_serializer import ProductsListSerializer
from api.services.product.get_product_by_category import GetProductByCategoryService


class GetProductByCategoryView(APIView):
    def get(self, request, **kwargs):
        products = GetProductByCategoryService.execute(kwargs)
        serializer = ProductsListSerializer(products, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)