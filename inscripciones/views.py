from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inscripciones.models import Inscripcion, LineaInscripcion 
from carro.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_inscripcion(request):
    inscripcion=Inscripcion.objects.create(user=request.user)
    carro=Carro(request)
    lineas_inscripcion=list()
    for key, value in carro.carro.items():
        lineas_inscripcion.append(LineaInscripcion(

            curso_id=key,
            user=request.user,
            inscripcion=inscripcion
        ))
    
    LineaInscripcion.objects.bulk_create(lineas_inscripcion)

    enviar_mail(
        inscripcion=inscripcion,
        lineas_inscripcion=lineas_inscripcion,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    return redirect ("../cursos")

def enviar_mail(**kwargs):
    
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/inscripcion.html",{
        "inscripcion": kwargs.get("inscripcion"),
        "lineas_inscripcion": kwargs.get("lineas_inscripcion"),
        "nombreusuario": kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)
    from_email="santiagosop2003@gmail.com"
    to=kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje)

    


