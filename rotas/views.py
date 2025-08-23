from django.shortcuts import render
import json
from django.http import JsonResponse
from django.conf import settings
import os

# Função para carregar dados dos pontos turísticos
def carregar_dados_pontos_turisticos():
    # Define o caminho completo do arquivo JSON
    caminho_arquivo = os.path.join(settings.BASE_DIR, 'data', 'pontos_turisticos.json')
    pontos = []
    pontos_completo = []
    try:
        # Carrega os dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            pontos_completo = json_data

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
                'coords': item['coords'],
                'imagem': item['imagem'],
                'id': item['id'],
            }

            pontos.append(ponto)
    except FileNotFoundError:
        # Retorna uma lista vazia caso o arquivo JSON não seja encontrado
        pass

    return pontos, pontos_completo

# View para a página de rotas
def rotas(request):
    print('Rotas')

    # Carrega os pontos turísticos do JSON (ou usa dados estáticos se não for necessário ler o JSON)
    pontos, _ = carregar_dados_pontos_turisticos()
    _ , pontos_completos = carregar_dados_pontos_turisticos()

    #endereco_detalhe = 'guia_turistico:detalhes_ponto_turistico'

    # Unir `context` e `pontos` em um único dicionário
    context = {
        'nome_da_pagina': 'Rotas',
        'nome_do_app': 'rotas',
        'nome_do_escopo': 'rotas',
        'exibir_botao': True,
        'botao_click': True,
        'nome_botao': 'Adicionar à Rota',  # ou outro texto para o botão
        'frase_login': 'Realize login para adicionar à rota.',
        'pontos': pontos,
        'pontos_completos': pontos_completos,
        'card_rota': True,
        'nome_detalhe': 'detalhes_ponto_turistico',
        #'endereco_detalhe': endereco_detalhe
    }

    return render(request, 'rotas/mapa_rota.html', context)

# Outras views
def minha_rota(request):
    print("Minha Rota")

    _, pontos_completo = carregar_dados_pontos_turisticos()
    ponto = pontos_completo

    context = {
        'nome_da_pagina': 'Minha Rota',
        'nome_do_app': 'minha_rota',
        'nome_do_escopo': 'rotas',
        'pontos': ponto,
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

# Função para salvar dados no arquivo JSON
def salvar_historico_pontos(request):
    if request.method == "POST":
        # Captura os dados JSON diretamente do corpo da requisição
        try:
            dados = json.loads(request.body)  # Carrega o JSON enviado no corpo da requisição
        except json.JSONDecodeError:
            return JsonResponse({"error": "Dados inválidos"}, status=400)
        
        # Aqui você pode salvar os dados no arquivo JSON ou banco de dados
        try:
            # Salvando os dados no arquivo JSON
            with open('pontos_roteiro.json', 'w') as f:
                json.dump(dados, f)
                
            return JsonResponse({"message": "Dados salvos com sucesso!"})
        
        except Exception as e:
            return JsonResponse({"error": f"Ocorreu um erro ao salvar os dados: {str(e)}"}, status=500)
    
    return JsonResponse({"error": "Método não permitido"}, status=405)

def avaliacao_rota(request):
    print ("Avaliacao Rota Turistica")

    context = {
        'nome_da_pagina': 'Avaliação Rota Turistica',
        'nome_do_app': 'avaliacao_rota',
        'nome_do_escopo': 'rotas',
        'frase_pergunta': 'Como foi sua rota de viagens?',
    }

    return render(
        request,
        'rotas/avaliar_rota.html', context
    )

def adicionar_rota(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            nome = data.get("nome")
            endereco = data.get("endereco")
            
            # Aqui você pode salvar os dados em um arquivo JSON ou no banco de dados
            # Exemplo simples de salvar em um arquivo JSON

            # Lê o arquivo JSON existente
            try:
                with open('rotas.json', 'r') as f:
                    rotas = json.load(f)
            except FileNotFoundError:
                rotas = []

            # Adiciona o novo ponto turístico
            rotas.append({"nome": nome, "endereco": endereco})

            # Salva o arquivo JSON atualizado
            with open('rotas.json', 'w') as f:
                json.dump(rotas, f)

            return JsonResponse({"success": True})
        
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Método inválido."})