from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

from conf import settings


class CustomPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']  # Количество объектов на странице по умолчанию
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества объектов на странице
    max_page_size = 100