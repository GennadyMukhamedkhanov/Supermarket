import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView


class GetDecodingToken(APIView):
    def get_decode(self, token):
        try:
            # Декодирование токена
            payload = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
            user_id = payload.get('id')
            username = payload.get('username')

            return user_id, username
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

    def get_token(self, request):
        return request.META.get('HTTP_AUTHORIZATION').split()[1]
