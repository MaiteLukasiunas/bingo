from src import bingo

mi_carton = bingo.carton

def test_que_no_se_repitan():
    assert bingo.no_celdas_repetidas(mi_carton)

