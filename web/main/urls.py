from django.urls import path
from . import views

urlpattarns = [
  path('', views.index, name='index')
]