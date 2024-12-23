from django.db import models


class Category(models.Model):
    # Название категории продукта
    name = models.CharField(max_length=255, verbose_name='Имя')
    # Уникальный слаг для категории (используется в URL)
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        db_table = 'Category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = 'db'

    def __str__(self):
        return self.name  # Возвращает имя категории при вызове str()
