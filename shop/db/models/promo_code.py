from django.db import models
import random
import string
class PromoCode(models.Model):
    # Код промокода (должен быть уникальным)
    code = models.CharField(max_length=50, unique=True, verbose_name='Промокод')
    # Процент скидки, предоставляемый промокодом
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент скидки')
    # Дата начала действия промокода
    valid_from = models.DateTimeField(verbose_name='Дата начала действия')
    # Дата окончания действия промокода
    valid_to = models.DateTimeField(verbose_name='Дата окончания действия')
    # Флаг, указывающий, активен ли промокод
    is_active = models.BooleanField(default=True, verbose_name='Активен')



    class Meta:
        db_table = 'PromoCode'
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
        app_label = 'db'

    def __str__(self):
        return self.code

    def generate_code(self):
        length = 10
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def save(self, *args, **kwargs):
        if not self.code:  # Если код не установлен, генерируем новый
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = self.generate_code()
            if not PromoCode.objects.filter(code=code).exists():
                return code
