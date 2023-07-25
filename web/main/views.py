from django.shortcuts import render
from django.views.generic import ListView
from .models import Home
# Create your models here.

class LoginPageView(ListView):
    template_name = 'pages/page1.html'
    model = Home

# Create your views here.
