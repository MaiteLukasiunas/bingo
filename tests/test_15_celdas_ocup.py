from src import bingo

mi_carton = bingo.carton

def test_validar_quince_numeros():
    assert bingo.contar_celdas_ocupadas(mi_carton)

