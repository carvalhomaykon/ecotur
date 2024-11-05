from django.shortcuts import render

# Create your views here.
def rotas(request):
    print('Rotas')

    context = {
        'nome_da_pagina': 'Rotas',
        'nome_do_app': 'rotas',
        'nome_do_escopo': 'rotas',
    }

    return render(
        request,
        'rotas/mapa_rotas.html', context
    )