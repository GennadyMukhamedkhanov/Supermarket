from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions.user import IsAuthor
from api.serializers.user.user_serializer import UserDataSerializer
from api.services.user.create import CreateUsersService
from api.services.user.update import UserUpdateService
from api.views.token.decoding import GetDecodingToken
from db.models import User


class GetCreateUpdateUserView(APIView):

    def get(self, request):
        self.permission_classes = [IsAuthenticated, IsAuthor]
        self.check_permissions(request)
        get_decoding_token = GetDecodingToken()
        token = get_decoding_token.get_token(request)
        self.user_id, self.username = get_decoding_token.get_decode(token)
        obj = get_object_or_404(User, id=self.user_id)
        self.check_object_permissions(
            request=request,
            obj=obj)

        user = UserDataSerializer(obj).data
        return Response(user, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        self.permission_classes = [AllowAny, ]
        self.check_permissions(request)
        CreateUsersService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        self.permission_classes = [IsAuthenticated, IsAuthor]
        self.check_permissions(request)

        get_decoding_token = GetDecodingToken()
        token = get_decoding_token.get_token(request)

        self.user_id, self.username = get_decoding_token.get_decode(token)
        obj = get_object_or_404(User, id=self.user_id)
        self.check_object_permissions(
            request=request,
            obj=obj)
        obj = UserUpdateService.execute(request.data | {'id': obj.id})
        user = UserDataSerializer(obj).data

        return Response(user, status=status.HTTP_200_OK)
