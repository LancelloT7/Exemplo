from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login

import json


def cadastrar(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        confirma = request.POST.get('confirmar_senha')

        if User.objects.filter(username=nome).exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe' )
            return render (request, 'cadastro.html')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Minimo de 6 caracteres para senha')
            return render (request, 'cadastro.html')
        if not senha == confirma:
            messages.add_message(request, constants.ERROR, 'Os campos de senha e confirmar senha devem ser iguais')  
            return render(request, 'cadastro.html')
        else:
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            usuario = User(username=nome)
            usuario.set_password(senha)
            usuario.save()
        
        
    return render(request, 'login.html')


def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('login')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('listar')  # Certifique-se de que 'listar' é o nome da URL no seu urls.py
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos')
            return render (request, 'login.html')  


# Create your views here.


def listar(request):

    usuarios = User.objects.all()
    return render (request, 'listar.html', {'usuarios':usuarios})
