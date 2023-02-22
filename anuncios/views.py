from django.shortcuts import render
from anuncios.models import Anuncio, Categoria

# Create your views here.

def anuncios(request):

    anuncios=Anuncio.objects.all()
    return render(request, "anuncios/anuncios.html", {"anuncios": anuncios})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    anuncios=Anuncio.objects.filter(categorias=categoria)
    return render(request, "anuncios/categoria.html", {'categoria':categoria, "anuncios": anuncios})

