# Generated by Django 3.0.4 on 2020-04-16 02:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200416_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='image',
            field=models.ImageField(default='pepporoni.jpg', storage=django.core.files.storage.FileSystemStorage(location='.menu/static/topImg'), upload_to=''),
        ),
    ]
