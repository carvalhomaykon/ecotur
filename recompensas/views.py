from django.shortcuts import render

# Create your views here.
def recompensas(request):
    print('Recompensas')

    return render(
        request,
        'recompensas/inicial_recompensas.html',
    )