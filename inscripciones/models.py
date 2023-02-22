from django.db import models
from django.contrib.auth import get_user_model
from cursos.models import Cursos
from django.db.models import F, Sum, FloatField

# Create your models here.

User=get_user_model()

class Inscripcion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineainscripcion_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
            
        )["total"]

    class Meta:
        db_table='inscripciones'
        verbose_name='inscripcion'
        verbose_name_plural='inscripciones'
        ordering=['id']

class LineaInscripcion(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Cursos, on_delete=models.CASCADE)
    inscripcion=models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inscrito a {self.curso.nombre}'

    class Meta:
        db_table='lineainscripciones'
        verbose_name='Linea Inscripcion'
        verbose_name_plural='Lineas Inscripciones'
        ordering=['id']