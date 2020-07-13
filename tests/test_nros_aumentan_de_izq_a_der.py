from src import bingo

mi_carton = bingo.carton

def test_nros_aumentan_de_izq_a_der():
    assert bingo.aumentan_de_izq_a_der(mi_carton)
