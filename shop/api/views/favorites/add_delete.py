from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.favorites.get import FavoritesSerializer
from api.services.favorites.add import AddProductsInFavoritesService
from api.services.favorites.delete import DeleteProductsInFavoritesService


class AddDeleteProductsInFavoritesView(APIView):
    def post(self, request, **kwargs):
        favorite = AddProductsInFavoritesService.execute(kwargs | {'user': request.user})
        serializer = FavoritesSerializer(favorite).data

        return Response(serializer)

    def delete(self, request, **kwargs):
        DeleteProductsInFavoritesService.execute(kwargs | {'user': request.user})

        return Response(status=status.HTTP_204_NO_CONTENT)
