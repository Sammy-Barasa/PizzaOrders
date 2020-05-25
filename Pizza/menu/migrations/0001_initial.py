# Generated by Django 3.0.4 on 2020-04-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pizza', models.CharField(choices=[('Regular', 'Regular Pizza'), ('Sicilian', 'Sicilian Pizza')], max_length=20)),
                ('flavour', models.CharField(choices=[('cheese', 'cheese'), ('1', '1-topping'), ('2', '2-toppings'), ('3', '3-toppings')], max_length=20)),
                ('size', models.CharField(choices=[('Large', 'Large'), ('Small', 'Small')], max_length=20)),
                ('toppings', models.ManyToManyField(to='menu.Topping')),
            ],
        ),
    ]