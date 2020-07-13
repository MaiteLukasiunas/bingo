from src import bingo

mi_carton = bingo.carton

def test_no_mas_de_2_celdas_vacias_consec_x_fila():
    assert bingo.sin_mas_de_2_celdas_vacias_consec_x_fila(mi_carton)
