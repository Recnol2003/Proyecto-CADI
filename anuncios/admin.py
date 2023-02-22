from django.contrib import admin
from .models import Categoria, Anuncio

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class AnuncioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Anuncio,AnuncioAdmin)

