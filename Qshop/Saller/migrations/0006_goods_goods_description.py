# Generated by Django 2.2.1 on 2019-09-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0005_goodstype_type_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(default='好好。。。。。'),
        ),
    ]
