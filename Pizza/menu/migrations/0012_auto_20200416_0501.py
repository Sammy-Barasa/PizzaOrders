# Generated by Django 3.0.4 on 2020-04-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20200416_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='image',
            field=models.ImageField(default='pep.jpg', upload_to='topimage'),
        ),
    ]
