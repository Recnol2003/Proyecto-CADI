import pytest
from cursos.models import Cursos, CategoriaCursos

def test_curso_creation():
    curso = Cursos(
        nombre='curso1',
        precio=1500
    )
    assert curso.nombre == 'curso1'

def test_categoria_creation():
    categoria = CategoriaCursos(
        nombre='categoria1',
    )
    assert categoria.nombre == 'categoria1'