from django.urls import path
from . import views

urlpatterns = [
    path('', views.anuncios, name="Anuncios"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
]