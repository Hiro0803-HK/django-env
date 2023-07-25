from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.LoginPageView.as_view()),
]