from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.services.email.sending import EmailService


class SendingEmailView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        code = EmailService.execute(request.data)

        return Response({'code': code}, status=status.HTTP_200_OK)
