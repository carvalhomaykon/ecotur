from django.shortcuts import render
import json
from django.conf import settings
import os

def carregar_dados_pontos_turisticos():
    # Define o caminho completo do arquivo JSON
    caminho_arquivo = os.path.join(settings.BASE_DIR, 'data', 'recompensas.json')
    pontos = []
    
    try:
        # Carrega os dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Processa os dados para filtrar e renomear campos
        for item in json_data:
            ponto = {
                'nome': item['nome'],
                'Tipo': item['tipo'],
                'Preco': item['preco']
            }

            pontos.append(ponto)
    except FileNotFoundError:
        # Caso o arquivo JSON não seja encontrado, ambos os arrays são mantidos vazios
        pass

    return pontos

# Create your views here.
def recompensas(request):
    print('Recompensas')

    context = {
        'nome_da_pagina': 'Recompensas',
        'nome_do_app': 'recompensas',
        'nome_do_escopo': 'recompensas',
    }

    return render(
        request,
        'recompensas/inicial_recompensas.html', context
    )

def resgate_recompensas(request):
    print('Regate de Recompensas')

    pontos = carregar_dados_pontos_turisticos()

    context = {
        'nome_da_pagina': 'Resgatar Recompensas',
        'nome_do_app': 'resgate_recompensas',
        'nome_do_escopo': 'resgate_recompensas',
        'exibir_botao': True,
        'nome_botao': 'Resgatar',
        'pontos': pontos
    }

    return render(
        request,
        'recompensas/resgate_recompensas.html', context
    )