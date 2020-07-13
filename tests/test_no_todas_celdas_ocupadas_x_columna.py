from src import bingo

mi_carton = bingo.carton

def test_no_todas_celdas_ocupadas_x_column():
    assert bingo.no_todas_las_celdas_de_column_ocup(mi_carton)
