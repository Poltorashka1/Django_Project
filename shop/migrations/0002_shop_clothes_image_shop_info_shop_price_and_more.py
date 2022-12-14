# Generated by Django 4.1.1 on 2022-09-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='clothes_image',
            field=models.ImageField(blank=True, upload_to='clothes_media/', verbose_name='Clothes photo'),
        ),
        migrations.AddField(
            model_name='shop',
            name='info',
            field=models.TextField(blank=True, max_length=1000, verbose_name='info_about_clothes'),
        ),
        migrations.AddField(
            model_name='shop',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name of clothes'),
        ),
    ]
