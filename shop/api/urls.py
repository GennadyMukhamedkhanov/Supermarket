from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.email.sending import SendingEmailView
from api.views.product.list import ProductsListView
from api.views.token.get import CustomTokenObtainPairView
from api.views.user.get_create_update import GetCreateUpdateUserView

urlpatterns = [
    # Получение токена
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Обновление токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Проверка токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Создание, получение и изменение пользователя
    path('user/', GetCreateUpdateUserView.as_view(), name='user'),

    # Отправка 4-х значного кода на почту
    path('sending_email_confirmation_code/', SendingEmailView.as_view(), name='sending_email'),

    # Получение списка всех товаров с пагинацией
    path('products/', ProductsListView.as_view(), name='products'),


    path('products/categories/', ProductsListView.as_view(), name='products'),

]
