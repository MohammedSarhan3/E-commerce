# Generated by Django 4.2 on 2024-01-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_product',
            name='Quantity',
            field=models.IntegerField(default=1),
        ),
    ]
