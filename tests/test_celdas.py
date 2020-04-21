from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador == 15

def test_menor_quince():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador > 14

def test_mayor_quince():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador < 16

def test_al_menos_una_ocupada():
    contador = 0
    contador2 = 9
    mi_carton = carton()
    
    for i in range(contador2):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) >= 1:
            contador += 1

    assert contador == contador2

def test_no_filas_vacias():
    contador = 0
    contador1 = 0
    contador2 = 0
    cont_final = 0
    mi_carton = carton()
    
    for celda in mi_carton[0]:
        contador = contador + celda
    for celda in mi_carton[1]:
        contador1 = contador1 + celda
    for celda in mi_carton[2]:
        contador2 = contador2 + celda

    if (contador >= 1):
        cont_final+=1
    if (contador1 >= 1):
        cont_final+=1
    if (contador2 >= 1):
        cont_final+=1
    assert cont_final == 3
