# Generated by Django 5.1.4 on 2024-12-21 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0016_promocode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=255)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db.order')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
                'db_table': 'Payment',
            },
        ),
    ]
