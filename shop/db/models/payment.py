from django.db import models

from db.models import Order


class Payment(models.Model):
    STATUS_CHOICES = [
        ('card', 'Оплата банковской картой'),
        ('cash', 'Оплата наличными при получении товара'),

    ]
    # Связь с заказом (один платеж принадлежит одному заказу)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    # Дата и время платежа
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время платежа')
    # Сумма платежа
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа')
    # Метод оплаты (например, Stripe или PayPal)
    payment_method = models.CharField(max_length=10, choices=STATUS_CHOICES, default='card', verbose_name='Метод оплаты')
    # Идентификатор транзакции
    transaction_id = models.CharField(max_length=255, verbose_name='Идентификатор транзакции')

    class Meta:
        db_table = 'Payment'
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        app_label = 'db'

    def __str__(self):
        return f"Payment for Order {self.order.id}"
