from django.shortcuts import render

# Create your views here.
def avaliacao(request):
    print('Avaliação')

    return render(
        request,
        'avaliacao/avaliacao.html',
    )