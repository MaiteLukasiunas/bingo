from src.bingo import carton

def test_que_no_se_repitan():
    contador = 0
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    carton = (
            (12,10,0,0,6,0,0,2,0),
            (15,0,7,0,3,4,5,0,66),
            (8,20,0,1,0,0,33,0,45)
        )
    for contador1 in range(0, 3):
        for contador2 in range(0, 9):
                for contador3 in range(contador1, 3):
                    for contador4 in range(contador2, 9):
                        if carton[contador1][contador2] == carton[contador3][contador4]:
                            if carton[contador1][contador2] != 0:
                                contador += 1
    assert contador == 15


