from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.services.cart.add import AddProductInCartService


class AddProductInCartUser(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, **kwargs):
        AddProductInCartService.execute({
            'id': kwargs.get('id'),
            'user': request.user,
            'amount_goods': request.query_params['amount_goods']
        })

        return Response(status=status.HTTP_201_CREATED)
