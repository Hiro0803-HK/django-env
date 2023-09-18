from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Home
# Create your models here.

class LoginPageView(ListView):
    template_name = 'pages/page1.html'
    model = Home

class TopPageView(ListView):
    template_name = 'pages/page0.html'
    model = Home
# Create your views here.



