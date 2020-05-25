from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='menu'),
    path('offers/',views.offers, name='offers')
]