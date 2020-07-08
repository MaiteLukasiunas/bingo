from src.bingo import carton

def test_no_mas_de_2_celdas_ocup_consec_x_fila():
    contador2 = 0
    contador1 = 0
    contador = 0

    mi_carton = carton()
    for contador in range(0, 3):
        for contador1 in range(0, 7):
            if (mi_carton[contador][contador1] > 0 and mi_carton[contador][contador1+1] > 0 and mi_carton[contador][contador1+2] > 0):
                contador2 += 1
    assert contador2 == 0;

