# Generated by Django 3.0.4 on 2020-04-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='image',
            field=models.ImageField(default='pep.jpg', upload_to='topimages'),
        ),
    ]
