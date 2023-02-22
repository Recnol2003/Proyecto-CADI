from django.shortcuts import render, redirect

from .carro import Carro

from cursos.models import Cursos

# Create your views here.

def agregar_curso(request, curso_id):
    
    carro=Carro(request)

    curso=Cursos.objects.get(id=curso_id)

    carro.agregar(curso=curso)

    return redirect("Cursos")

def eliminar_curso(request, curso_id):
    
    carro=Carro(request)

    curso=Cursos.objects.get(id=curso_id)

    carro.eliminar(curso=curso)

    return redirect("Cursos")

def restar_curso(request, curso_id):
    
    carro=Carro(request)

    curso=Cursos.objects.get(id=curso_id)

    carro.restar(curso=curso)

    return redirect("Cursos")

def limpiar_carro(request, curso_id):
    
    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Cursos")

