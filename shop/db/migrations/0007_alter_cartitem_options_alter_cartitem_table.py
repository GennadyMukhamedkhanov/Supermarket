# Generated by Django 5.1.4 on 2024-12-20 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_cartitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Товар в корзине', 'verbose_name_plural': 'Товар в корзине'},
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='CartItem',
        ),
    ]
