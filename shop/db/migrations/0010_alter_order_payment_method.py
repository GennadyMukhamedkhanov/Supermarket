# Generated by Django 5.1.4 on 2024-12-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_alter_order_created_at_alter_order_is_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Оплата банковской картой'), ('cash', 'Оплата наличными при получении')], default='card', max_length=10),
        ),
    ]
