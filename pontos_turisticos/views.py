from django.shortcuts import render

# Create your views here.
def pontos_turisticos(request):
    print('Pontos Turisticos')

    context = {
        'nome_da_pagina': 'Pontos Turisticos',
        'nome_do_app': 'pontos_turisticos',
        'nome_do_escopo': 'pontos_turisticos',
    }

    return render(
        request,
        'pontos_turisticos/pontos_turisticos.html', context
    )

def historia_pt(request):
    print('História Pontos Turisticos')

    return render(
        request,
        'pontos_turisticos/historias_pt.html',
    )