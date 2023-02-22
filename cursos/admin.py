from django.contrib import admin
from .models import CategoriaCursos, Cursos

#Register your models here

class CategoriaCursosAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class CursosAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(CategoriaCursos, CategoriaCursosAdmin)

admin.site.register(Cursos, CursosAdmin)



