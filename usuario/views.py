# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

# View de login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Usa auth_login para evitar conflito com a função login
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'usuario/login_ecotour.html')

# View de cadastro
def cadastro(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já está em uso.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
        else:
            # Cria um novo usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Conta criada com sucesso! Você já pode fazer login.")
            return redirect("login")

    return render(request, 'usuario/registro_ecotour.html')

# View de logout
def user_logout(request):
    auth_logout(request)  # Usa auth_logout para evitar conflito com a função user_logout
    return redirect('home')  # Redireciona para a página inicial ou outra página
