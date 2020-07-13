from src import bingo

mi_carton = bingo.carton

def test_solo_3_colum_con_1_celda_ocup():
    assert bingo.solo_3_colum_con_1_celda_ocup(mi_carton)
