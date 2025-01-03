from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions.user import IsAdmin
from api.serializers.product.list_serializer import ProductsListSerializer
from api.services.product.create import ProductsCreateService


class ProductsCreateView(APIView):
    permission_classes = [IsAdmin, ]

    def post(self, request, **kwargs):
        product = ProductsCreateService.execute(request.data, {'image': request.data.get('image')})
        serializer = ProductsListSerializer(product).data
        return Response(serializer)
    
