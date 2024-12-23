from django.db import models

from db.models import Order, Product


class OrderItem(models.Model):
    # Связь с заказом (один элемент заказа принадлежит одному заказу)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    # Связь с продуктом (один элемент заказа связан с одним продуктом)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    # Количество данного продукта в заказе
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    # Цена продукта на момент покупки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на момент покупки')

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
        app_label = 'db'

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
