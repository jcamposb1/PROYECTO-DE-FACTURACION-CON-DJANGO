from django.shortcuts import render


def index(request):
    opcion = {
        'menu': 'Menu',
    }

    return render(request,'principal.html', opcion)