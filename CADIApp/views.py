import re
from django.shortcuts import render, HttpResponse

from carro.carro import Carro

def inicio(request):

    carro=Carro(request)

    return render(request, "CADIApp/inicio.html")

# Create your views here.
