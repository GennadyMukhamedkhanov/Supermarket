from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.cart_item.list import ListProductsInCartSerializer
from api.services.cart.list import ListProductsInCartService


class ListProductsInCartUser(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, **kwargs):
        products = ListProductsInCartService.execute({
            'user': request.user,
                   })
        serializer = ListProductsInCartSerializer(products, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
