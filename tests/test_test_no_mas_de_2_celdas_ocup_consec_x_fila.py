from src import bingo

mi_carton = bingo.carton

def test_no_mas_de_2_celdas_ocup_consec_x_fila():
    assert bingo.no_mas_de_2_celdas_ocup_consec_x_fila(mi_carton)

