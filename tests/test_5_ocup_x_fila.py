from src.bingo import carton

def test_5_ocupadas_x_fila():
    contador = 0
    contador2 = 3
    mi_carton = carton()

    for i in range(contador2):
        if (mi_carton[i][0] + mi_carton[i][1] + mi_carton[i][2] + mi_carton[i][3] + mi_carton[i][4] + mi_carton[i][5] + mi_carton[i][6] + mi_carton[i][7] + mi_carton[i][8]) == 5:
            contador += 1

    assert contador == 3;
