from django.shortcuts import render
import json
from django.conf import settings
import os

def carregar_dados_pontos_turisticos():
    # Define o caminho completo do arquivo JSON
    caminho_arquivo = os.path.join(settings.BASE_DIR, 'data', 'guia_turistico.json')
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
                'nome': item.get('nome'),  # Renomeia o campo 'nome' para 'Nome'
                'Descricao': item.get('descricao'),
                'Nome Guia': item.get('nome_guia'),
                'Preço': item.get('preco'),
                'Horario': item.get('horario'),
                'Idiomas': item.get('idiomas'),
                'id': item.get('id'),
                'whatsapp': item.get('whatsapp'),
                'imagem': item.get('imagem'),
            }
            pontos.append(ponto)    
    except FileNotFoundError:
        # Caso o arquivo JSON não seja encontrado, ambos os arrays são mantidos vazios
        pass

    return pontos, pontos_completo

# Create your views here.
def guia_turistico(request):
    print('Guia Turistico')

    pontos, _ = carregar_dados_pontos_turisticos()

    context = {
        'nome_da_pagina': 'Guia Turistico',
        'nome_do_app': 'guia_turistico',
        'nome_do_escopo': 'guia_turistico',
        'exibir_botao': True,
        'nome_botao': 'Entrar em Contato',
        'frase_login': 'Realize login para entrar em contato.',
        'botao_click': False,
        'card_rota': False,
        'nome_detalhe': 'detalhe_guia_turistico',
        'pontos': pontos,
    }

    return render(
        request,
        'guia_turistico/contratar_guia.html', context
    )

def detalhe_guia_turistico(request, id):
    print ("Contato Guia Turistico")

    # Carrega os dados do arquivo JSON, utilizando `pontos_completo` para acessar todos os dados
    _, pontos_completo = carregar_dados_pontos_turisticos()
    
    # Procura o ponto turístico pelo ID
    ponto = next((p for p in pontos_completo if int(p.get('id', -1)) == id), None)

    if ponto is None:
        # Caso o ponto turístico não seja encontrado, retorna uma página de erro
        return render(request, 'pontos_turisticos/erro.html')  # Ajuste conforme a necessidade

    context = {
        'nome_da_pagina': 'Detalhe Guia',
        'nome_do_app': 'detalhe_guia_turistico',
        'nome_do_escopo': 'guia_turistico',
        'ponto': ponto,
    }

    return render(
        request,
        'guia_turistico/detalhe_guia_turistico.html', context
    )

def avaliacao_guia(request, id):
    print ("Avaliacao Guia Turistico")

    context = {
        'nome_da_pagina': 'Avaliação Guia',
        'nome_do_app': 'avaliacao_guia',
        'nome_do_escopo': 'guia_turistico',
        'frase_pergunta': 'Como foi sua experiência com o guia?',
        'ponto': id,
        'nome_detalhe': 'detalhe_guia_turistico',
    }

    return render(
        request,
        'guia_turistico/avaliacao_guia.html', context
    )