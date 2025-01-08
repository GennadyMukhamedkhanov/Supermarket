from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.categories.list import ListCategoriesSerializer
from api.services.category.list import ListCategoriesService


class ListCategoriesView(APIView):
    def get(self, request):
        categories = ListCategoriesService.execute({})
        serializer = ListCategoriesSerializer(categories, many=True).data

        return Response(serializer)

