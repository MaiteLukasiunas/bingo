from src.bingo import carton

def test_solo_3_colum_con_1_celda_ocup():
    contador = 0
    contador2 = 9
    mi_carton = carton()

    for i in range(contador2):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) == 1:
            contador += 1

    assert contador == 3;
