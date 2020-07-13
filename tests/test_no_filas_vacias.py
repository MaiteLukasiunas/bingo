from src import bingo

mi_carton = bingo.carton

def test_no_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton)
