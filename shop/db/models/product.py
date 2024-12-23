from django.db import models

from db.models import Category


class Product(models.Model):
    # Название продукта
    name = models.CharField(max_length=255, verbose_name='Название')
    # Описание продукта
    description = models.TextField(verbose_name='Описание')
    # Цена продукта с максимальной длиной 10 цифр и 2 десятичными знаками
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    # Связь с категорией (один продукт принадлежит одной категории)
    category = models.ForeignKey(Category, related_name='products', related_query_name='product',
                                 on_delete=models.CASCADE, verbose_name='Категория')
    # Изображение продукта
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    # Количество продукта на складе
    stock = models.PositiveIntegerField(default=0, verbose_name='Остаток на складе')
    # Дата и время создания продукта
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # Дата и время последнего обновления продукта
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = 'Product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        app_label = 'db'

    def __str__(self):
        return self.name
