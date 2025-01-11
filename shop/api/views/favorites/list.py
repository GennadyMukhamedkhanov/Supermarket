from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.favorites.list_favorites_products import FavoritesProductsSerializer
from api.services.favorites.list_favorites_products import ListFavoritesProductService


class ListFavoritesProductView(APIView):
    def get(self, request, **kwargs):
        favorite = ListFavoritesProductService.execute({'user': request.user})
        serializer = FavoritesProductsSerializer(favorite, many=True).data

        return Response(serializer)
