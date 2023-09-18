from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.LoginPageView.as_view(), name='page1'),
    path('page0/', views.TopPageView.as_view(), name='page0'),
    path('', views.TopPageView.as_view(), name='page00'),

]