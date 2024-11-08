from django.shortcuts import render

# Create your views here.
def usuario(request):
    print('Usuário')

    return render(
        request,
        'usuario/login_ecotour.html',
    )

def cadastro(request):
    print ("Página de Cadastro")

    return render(
        request,
        'usuario/registro_ecotour.html'
    )