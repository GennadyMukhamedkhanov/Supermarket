from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавьте пользовательские данные в полезную нагрузку
        token['id'] = user.id
        token['username'] = user.username

        return token
