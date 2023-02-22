from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Anuncio(models.Model):
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="anuncios", null=True, blank=True)
    contenido=models.CharField(max_length=50, null=True, blank=True)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='anuncio'
        verbose_name_plural='anuncios'

    def __str__(self):
        return self.titulo

