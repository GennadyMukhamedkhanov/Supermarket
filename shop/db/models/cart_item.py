from django.db import models

from db.models import Cart, Product


class CartItem(models.Model):
    # Связь с корзиной (один элемент корзины принадлежит одной корзине)
    cart = models.ForeignKey(Cart, related_name='items', related_query_name='item',
                             verbose_name='Корзина', on_delete=models.CASCADE)
    # Связь с продуктом (один элемент корзины связан с одним продуктом)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Количество данного продукта в корзине
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'CartItem'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товар в корзине'
        app_label = 'db'

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
