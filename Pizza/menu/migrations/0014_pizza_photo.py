# Generated by Django 3.0.4 on 2020-04-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20200416_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(default='pepi.jpg', upload_to='pizzaimage'),
        ),
    ]
