# Generated by Django 2.2.1 on 2019-09-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_cart_goods_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_number',
            field=models.CharField(max_length=32, null=True),
        ),
    ]