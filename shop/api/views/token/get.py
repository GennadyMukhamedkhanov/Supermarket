from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers.token.custom_token_obtain_pair_serializer import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

