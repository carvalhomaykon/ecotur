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
        'rotas/mapa_rota.html', context
    )

def minha_rota(request):
    print ("Minha Rota")

    context = {
        'nome_da_pagina': 'Minha Rota',
        'nome_do_app': 'minha_rota',
        'nome_do_escopo': 'rotas',
    }

    return render(
        request,
        'rotas/minha_rota.html', context
    )

def historico_rota(request):
    print ("Historico Rota")

    context = {
        'nome_da_pagina': 'Histórico Rota',
        'nome_do_app': 'historico_rota',
        'nome_do_escopo': 'historico_rota',
    }

    return render(
        request,
        'rotas/historico_rota.html', context
    )