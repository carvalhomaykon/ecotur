from django.shortcuts import render

# Create your views here.
def home(request):
    print('Home')

    context = {
        'nome_da_pagina': 'Home',
        'nome_do_app': 'home',       # Nome do app
        'nome_do_escopo': 'home',  # Nome do escopo ou outra categoria
    }

    return render(
        request,
        'home/home.html', context
    )