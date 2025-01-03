from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AddProductInCartUser(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, **kwargs):
        pass