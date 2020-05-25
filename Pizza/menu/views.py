from django.shortcuts import render
from .models import Topping,  Pizza
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    formdata=request.POST.copy()
    context={
        'Tops':Topping.objects.all()
    }

    return render(request,'menu/index.html',context)


def offers(request):
    pizzas=Pizza.objects.all(),   
    
    context={
        'Pizza':pizzas,
    
    }

    return render(request,'menu/home.html',context)

def cart(request):
    pass