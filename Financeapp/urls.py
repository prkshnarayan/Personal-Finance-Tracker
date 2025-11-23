from django.urls import path
from Financeapp import views

urlpatterns = [
    path('', views.home, name='home')
]
