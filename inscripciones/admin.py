from django.contrib import admin
from .models import Inscripcion, LineaInscripcion
# Register your models here.

admin.site.register([Inscripcion, LineaInscripcion])