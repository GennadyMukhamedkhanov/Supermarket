from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .manager import CustomUserManager


class User(AbstractUser):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. Должно быть от 9 до 15 цифр."
    )
     # Поле для уникального номера телефона
    phone_number = models.CharField(max_length=15, validators=[phone_validator],
                                    blank=False, null=False, unique=True, verbose_name='Телефон')
    username = models.CharField(max_length=150, verbose_name='Имя')
    # Флаг, указывающий, является ли пользователь менеджером
    is_manager = models.BooleanField(default=False, verbose_name='Является менеджером')
#     # Флаг, указывающий, является ли пользователь администратором
    is_admin = models.BooleanField(default=False, verbose_name='Является админом')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']
    objects = CustomUserManager()



    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        app_label = 'db'

    def __str__(self):
        return self.username  # Возвращает имя пользователя при вызове str()




