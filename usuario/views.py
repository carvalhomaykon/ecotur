from django.shortcuts import render

# Create your views here.
def usuario(request):
    print('Usuário')

    return render(
        request,
        'usuario/login_ecotour.html',
    )