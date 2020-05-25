
from django.db import models

# Create your models here.

TYPES=[
    #(value,label)
    ('Regular','Regular Pizza'),
    ('Sicilian','Sicilian Pizza')
]

FLAVOURS=[
('cheese','cheese'),
('1','1-topping'),
('2','2-toppings'),
('3','3-toppings')
]
SIZES=[
    ('Large','Large'),
    ('Small','Small')
]

class Topping(models.Model):
    top=models.CharField(max_length=60)
    image=models.ImageField(upload_to='topimage',default='pepi.jpg')
    def __str__(self):
        return f'{self.top}'

class Pizza(models.Model):
    type_pizza=models.CharField(max_length=20, choices=TYPES)
    flavour=models.CharField(max_length=20, choices=FLAVOURS)
    size=models.CharField(max_length=20, choices=SIZES)
    toppings = models.ManyToManyField(Topping)
    photo=models.ImageField(upload_to='pizzaimage',default='pepi.jpg')
    def __str__(self):
        return f'{self.type_pizza},{self.flavour} to be topped with {self.toppings}({self.size})'

