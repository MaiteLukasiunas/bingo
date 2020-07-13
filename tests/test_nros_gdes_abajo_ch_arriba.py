from src import bingo

mi_carton = bingo.carton

def test_nros_gdes_abajo_ch_arriba():
    assert bingo.gdes_abajo_ch_arriba(mi_carton)
