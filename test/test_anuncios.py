import pytest
from anuncios.models import Anuncio, Categoria

def test_anuncio_creation():
    anuncio = Anuncio(
        titulo='anuncio1'
    )
    assert anuncio.titulo == 'anuncio1'

def test_categoria_creation():
    categoria = Categoria(
        nombre='categoria1'
    )
    assert categoria.nombre == 'categoria1'