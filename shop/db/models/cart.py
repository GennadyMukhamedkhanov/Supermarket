from django.db import models

from db.models import User


class Cart(models.Model):
    # Связь с пользователем (один пользователь может иметь только одну корзину)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='cart')
    # Дата и время создания корзины
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')

    class Meta:
        db_table = 'Cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        app_label = 'db'

    def __str__(self):
        return f"Cart of {self.user.username}"
