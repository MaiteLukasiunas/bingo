def carton():
    mi_carton = (
            (1,1,0,1,1,1,0,1,1),
            (0,0,1,0,0,0,0,0,0),
            (1,0,1,0,1,1,1,1,1)
        )
    return  mi_carton

def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias == 15
