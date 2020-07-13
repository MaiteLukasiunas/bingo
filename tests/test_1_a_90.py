from src import bingo

mi_carton = bingo.carton

def test_uno_a_noventa():
    assert bingo.nros_del_1_al_90(mi_carton);
