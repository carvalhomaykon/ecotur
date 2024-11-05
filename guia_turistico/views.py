from django.shortcuts import render

# Create your views here.
def guia_turistico(request):
    print('Guia Turistico')

    return render(
        request,
        'guia_turistico/contratar_guia.html',
    )   