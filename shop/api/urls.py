from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.email.sending import SendingEmailView
from api.views.token.get import CustomTokenObtainPairView
from api.views.user.create import CreateUserView

urlpatterns = [
    # Получение токена
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Обновление токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Проверка токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Создание пользователя
    path('user/', CreateUserView.as_view(), name='user'),


    path('sending_email_confirmation_code/', SendingEmailView.as_view(), name='sending_email'),

]
