from django.db import models

from db.models import User, Product


class Favorite(models.Model):
    # Связь с пользователем (один элемент избранного принадлежит одному пользователю)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    # Связь с продуктом (один элемент избранного связан с одним продуктом)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        db_table = 'Favorite'
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
        app_label = 'db'
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.product.name} favorited by {self.user.username}"
