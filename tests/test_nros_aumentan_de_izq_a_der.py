def test_nros_aumentan_de_izq_a_der():
    contador = 0
    contador1 = 0
    carton = (
            (1,4,5,0,6,8,0,9,10),
            (11,0,13,0,0,15,0,17,0),
            (0,23,0,44,0,59,0,0,62)
            )
    for contador in range(0, 3):
        for contador1 in range(0, 8):
            if carton[contador][contador1] != 0 and carton[contador][contador1+1] != 0:
                assert (carton[contador][contador1] < carton[contador][contador1+1])
