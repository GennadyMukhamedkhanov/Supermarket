from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions.user import IsAdmin
from api.serializers.product.get import GetProductSerializer
from api.services.product.delete import DeleteProductService
from api.services.product.get import GetProductService
from api.services.product.update import UpdateProductService


class GetUpdateDeleteProductView(APIView):
    def get(self, request, **kwargs):
        product = GetProductService.execute(kwargs)
        serializer = GetProductSerializer(product).data

        return Response(serializer)

    def put(self, request, **kwargs):
        self.permission_classes = [IsAdmin, ]
        self.check_permissions(request)
        product = UpdateProductService.execute(request.data | kwargs)
        serializer = GetProductSerializer(product).data

        return Response(serializer)

    def delete(self, request, **kwargs):
        self.permission_classes = [IsAdmin, ]
        self.check_permissions(request)
        DeleteProductService.execute(kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)
