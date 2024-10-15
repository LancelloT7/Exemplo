from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.logar, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('listar/', views.listar, name='listar'),
]
