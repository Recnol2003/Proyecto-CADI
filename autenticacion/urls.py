from django.urls import path
from .views import Registro, cerrar_sesion, logear

urlpatterns = [
    path('', Registro.as_view(), name="Autenticacion"),
    path('login', logear, name="login"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
]
