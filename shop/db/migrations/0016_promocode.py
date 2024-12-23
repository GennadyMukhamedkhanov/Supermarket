# Generated by Django 5.1.4 on 2024-12-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0015_alter_favorite_product_alter_favorite_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Промокод')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Процент скидки')),
                ('valid_from', models.DateTimeField(verbose_name='Дата начала действия')),
                ('valid_to', models.DateTimeField(verbose_name='Дата окончания действия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
                'db_table': 'PromoCode',
            },
        ),
    ]
