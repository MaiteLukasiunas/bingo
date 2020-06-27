def test_nros_gdes_abajo_ch_arriba():
    contador = 0
    contador1 = 0
    carton = (
            (1,3,4,6,2,7,8,9,10),
            (10,12,11,20,13,14,15,20,21),
            (22,30,33,40,51,60,88,70,77)

        )
    for contador in range(0,9):
        if carton[0][contador] < carton[1][contador] and carton[1][contador] < carton[2][contador]:
            contador1 += 1

    assert contador1 == 9
