from django.shortcuts import render
import json
from django.conf import settings
import os

# Create your views here.
def carregar_dados_pontos_turisticos():
    # Define o caminho completo do arquivo JSON
    caminho_arquivo = os.path.join(settings.BASE_DIR, 'data', 'pontos_turisticos.json')
    pontos = []
    pontos_completo = []  # Armazena todos os dados do JSON

    try:
        # Carrega os dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            pontos_completo = json_data  # Mantém todos os dados originais

        # Processa os dados para filtrar e renomear campos
        for item in json_data:
            ponto = {
                'Nome': item.get('nome'),  # Renomeia o campo 'nome' para 'Nome'
                'Descricao': item.get('descricao'),
                'Dificuldade de Acesso': item.get('dificuldade_acesso'),
                'Tempo de Visita': item.get('tempo_visita'),
                'Distância': item.get('distancia'),
                'Tipo': item.get('tipo'),
                'Popularidade': item.get('popularidade'),
            }
            pontos.append(ponto)
    except FileNotFoundError:
        # Caso o arquivo JSON não seja encontrado, ambos os arrays são mantidos vazios
        pass

    return pontos, pontos_completo

def pontos_turisticos(request):
    print('Pontos Turisticos')

    _, pontos_completo = carregar_dados_pontos_turisticos()
    pontos = pontos_completo

    context = {
        'nome_da_pagina': 'Pontos Turisticos',
        'nome_do_app': 'pontos_turisticos',
        'nome_do_escopo': 'pontos_turisticos',
        'pontos': pontos,
    }

    return render(
        request,
        'pontos_turisticos/pontos_turisticos.html', context
    )

# Página de detalhes de um ponto turístico
def detalhes_ponto_turistico(request, id):
    # Carrega os dados do arquivo JSON, utilizando `pontos_completo` para acessar todos os dados
    _, pontos_completo = carregar_dados_pontos_turisticos()
    
    # Procura o ponto turístico pelo ID
    ponto = next((p for p in pontos_completo if int(p.get('id', -1)) == id), None)

    if ponto is None:
        # Caso o ponto turístico não seja encontrado, retorna uma página de erro
        return render(request, 'pontos_turisticos/erro.html')  # Ajuste conforme a necessidade

    context = {
        'nome_da_pagina': 'Detalhe Ponto Turístico',
        'nome_do_app': 'detalhes_ponto_turistico',
        'nome_do_escopo': 'pontos_turisticos',
        'ponto': ponto
    }
    return render(request, 'pontos_turisticos/detalhes_ponto.html', context)

def avaliacao_ponto(request, id):
    print ("Avaliacao Guia Turistico")

    context = {
        'nome_da_pagina': 'Avaliação Ponto Turistico',
        'nome_do_app': 'avaliacao_ponto',
        'nome_do_escopo': 'pontos_turisticos',
        'frase_pergunta': 'Como foi seu roteiro de viagens?',
        'ponto': id,
        'nome_detalhe': 'detalhes_ponto_turistico',
    }

    return render(
        request,
        'pontos_turisticos/avaliacao_ponto.html', context
    )