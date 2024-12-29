from rest_framework.response import Response
from rest_framework.views import APIView

from api.paginators.paginator import CustomPagination
from api.serializers.product.list_serializer import ProductsListSerializer
from api.services.product.list_service import ProductsListService


class ProductsListView(APIView):
    pagination_class = CustomPagination
    def get(self, request):
        products = ProductsListService.execute({})
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = ProductsListSerializer(paginated_products, many=True).data

        return paginator.get_paginated_response(serializer)
