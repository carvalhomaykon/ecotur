from django.shortcuts import render

# Create your views here.
def avaliacao_geral(request):
    print('Avaliação')

    context = {
        'nome_da_pagina': 'Sugestão',
        'nome_do_app': 'avaliacao_geral',       # Nome do app
        'nome_do_escopo': 'avaliacao_geral',  # Nome do escopo ou outra categoria
    }

    return render(
        request,
        'avaliacao_geral/avaliacao_geral.html', context
    )