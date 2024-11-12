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
            pontos = json_data  # Mantém todos os dados originais
        pontos.append(pontos)
    except FileNotFoundError:
        # Caso o arquivo JSON não seja encontrado, ambos os arrays são mantidos vazios
        pass

    return pontos

# Create your views here.
def recompensas(request):
    print('Recompensas')

    return render(
        request,
        'recompensas/inicial_recompensas.html',
    )

def regate_rescompensas(request):
    print('Regate de Recompensas')

    pontos = carregar_dados_pontos_turisticos()

    context = {
        'nome_da_pagina': 'Resgatar Recompensas',
        'nome_do_app': 'recompensas',
        'nome_do_escopo': 'guia_turistico',
        'exibir_botao': True,
        'nome_botao': 'Resgatar',
        'pontos': pontos
    }

    return render(
        request,
        'recompensas/recompensas.html', context
    )