from django.shortcuts import render
import json
from django.conf import settings
import os

# Função para carregar dados dos pontos turísticos
def carregar_dados_pontos_turisticos():
    # Define o caminho completo do arquivo JSON
    caminho_arquivo = os.path.join(settings.BASE_DIR, 'data', 'pontos_turisticos.json')
    pontos = []
    try:
        # Carrega os dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Processa os dados para filtrar e renomear campos
        for item in json_data:
            ponto = {
                'nome': item['nome'],
                'Descricao': item['descricao'],
                'Dificuldade de Acesso': item['dificuldade_acesso'],
                'Tempo de Visita': item['tempo_visita'],
                'Distância': item['distancia'],
                'Tipo': item['tipo'],
                'Popularidade': item['popularidade'],
            }
            pontos.append(ponto)
    except FileNotFoundError:
        # Retorna uma lista vazia caso o arquivo JSON não seja encontrado
        pass

    return pontos

# View para a página de rotas
def rotas(request):
    print('Rotas')

    # Carrega os pontos turísticos do JSON (ou usa dados estáticos se não for necessário ler o JSON)
    pontos = carregar_dados_pontos_turisticos()

    #endereco_detalhe = 'guia_turistico:detalhes_ponto_turistico'

    # Unir `context` e `pontos` em um único dicionário
    context = {
        'nome_da_pagina': 'Rotas',
        'nome_do_app': 'rotas',
        'nome_do_escopo': 'rotas',
        'exibir_botao': True,
        'nome_botao': 'Adicionar à Rota',  # ou outro texto para o botão
        'pontos': pontos,  # Inclui `pontos` no contexto
        #'endereco_detalhe': endereco_detalhe
    }

    return render(request, 'rotas/mapa_rota.html', context)

# Outras views
def minha_rota(request):
    print("Minha Rota")

    context = {
        'nome_da_pagina': 'Minha Rota',
        'nome_do_app': 'minha_rota',
        'nome_do_escopo': 'rotas',
    }

    return render(request, 'rotas/minha_rota.html', context)

def historico_rota(request):
    print("Histórico Rota")

    context = {
        'nome_da_pagina': 'Histórico Rota',
        'nome_do_app': 'historico_rota',
        'nome_do_escopo': 'rotas',
    }

    return render(request, 'rotas/historico_rota.html', context)

def avaliar_rota(request):
    print("Avaliar Rota")

    '''
    context = {
        'nome_da_pagina': 'Avaliar Rota',
        'nome_do_app': 'avaliar_rota',
        'nome_do_escopo': 'rotas',
    }
    '''

    return render(request, 'rotas/avaliar_rota.html')