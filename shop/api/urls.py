from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.cart.add import AddProductInCartUser
from api.views.category.list import ListCategoriesView
from api.views.email.sending import SendingEmailView
from api.views.product.create import ProductsCreateView
from api.views.product.get_product_by_category import GetProductByCategoryView
from api.views.product.get_update_delete import GetUpdateDeleteProductView
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
    path('products/', ProductsListView.as_view(), name='products_list'),
    # Создание нового товара (доступно только администратору)
    path('products/create/', ProductsCreateView.as_view(), name='product_create'),
    # Получение, обновление или удаление товара по его ID (GET/PUT/DELETE)
    path('product/<int:id>/', GetUpdateDeleteProductView.as_view(), name='product_get_update_delete'),
    # Получение списка категорий товаров (GET)
    path('product/categories/', ListCategoriesView.as_view(), name='list_categories'),
    # Получение товаров по категории (GET)
    path('products/<int:category_id>/', GetProductByCategoryView.as_view(), name='get_product_by_category'),





    # Добавление товара в корзину (POST)
    path('add_in_cart_product/<int:id>/', AddProductInCartUser.as_view(), name='add_product_cart'),

]
