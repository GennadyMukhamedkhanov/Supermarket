from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.serializers.cart_item.list import ListProductsInCartSerializer
from api.services.cart.add import AddProductInCartService
from api.services.cart_item.delete import DeleteProductsInCartService
from api.services.cart_item.update import UpdateAmountGoodsInCartProductsService


class UpdateAmountGoodsDeleteInCartProducts(APIView):
    permission_classes = [IsAuthenticated, ]

    def patch(self, request, **kwargs):
        obj = UpdateAmountGoodsInCartProductsService.execute({
            'id': kwargs.get('id'),
            'user': request.user,
            'amount_goods': request.query_params['amount_goods']
        })
        serializer = ListProductsInCartSerializer(obj).data

        return Response(serializer, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        DeleteProductsInCartService.execute({
            'id': kwargs.get('id'),
            'user': request.user,

        })

        return Response(status=status.HTTP_204_NO_CONTENT)
