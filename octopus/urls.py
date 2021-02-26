from django.urls import path 
from . import views

urlpatterns = [
    path('', views.tarifs_list, name='tarifs_list'),
]