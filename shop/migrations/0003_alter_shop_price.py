# Generated by Django 4.1.1 on 2022-09-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_clothes_image_shop_info_shop_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Price'),
        ),
    ]
