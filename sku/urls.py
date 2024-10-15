from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadSku, name='sku')
    
]