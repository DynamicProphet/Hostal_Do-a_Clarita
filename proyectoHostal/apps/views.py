from django.shortcuts import render
from .models import *
# Create your views here.


def pagina_principal(request):
    return render(request, 'pagina_principal.html', )

def home(request):
    contenidos = ContenidoWeb.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})