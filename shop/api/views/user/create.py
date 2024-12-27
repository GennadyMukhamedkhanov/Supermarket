from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.services.user.create import CreateUsersService


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        CreateUsersService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)
