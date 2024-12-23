from django.db import models

from db.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('card', 'Оплата банковской картой'),
        ('cash', 'Оплата наличными при получении товара'),

    ]

    # Связь с пользователем (один заказ принадлежит одному пользователю)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    # Дата и время создания заказа
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # Общая сумма заказа
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая сумма заказа')
    # Флаг, указывающий, был ли заказ оплачен
    is_paid = models.BooleanField(default=False, verbose_name='Сведения об оплате')
    # Метод оплаты (например, Stripe или PayPal)
    payment_method = models.CharField(max_length=10, choices=STATUS_CHOICES, default='card', verbose_name='Метод оплаты')

    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        app_label = 'db'

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
