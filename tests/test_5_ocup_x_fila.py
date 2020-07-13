from src import bingo

mi_carton = bingo.carton

def test_5_ocupadas_x_fila():
    assert bingo.x_fila_5_celdas_ocup(mi_carton)
