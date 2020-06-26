from src.bingo import carton
from src.bingo import validar_quince_numeros

def test_contar_celdas_ocupadas():
    carton = (
            (12,16,0,0,6,0,0,2,0),
            (15,0,9,0,3,4,5,0,10),
            (8,20,0,10,1,0,88,0,0)
        )
    assert validar_quince_numeros(carton) == True

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
