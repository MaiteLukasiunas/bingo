from src.bingo import carton

def test_no_todas_celdas_ocupadas_x_column():
    contador = 0
    contador2 = 9
    mi_carton = carton()

    for i in range(contador2):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) < 3:
            contador += 1

    assert contador == 9;
