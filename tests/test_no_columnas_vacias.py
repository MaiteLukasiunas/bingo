from src import bingo

mi_carton = bingo.carton

def test_al_menos_una_ocupada():
    assert bingo.no_columnas_vacias(mi_carton)
    
