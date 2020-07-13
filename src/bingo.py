import random
import math

def intentoCarton():
    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):

      contador = contador + 1

      if (contador == 50):
        return intentoCarton()

      numero = random.randint(1,90)

      columna = math.floor(numero / 10)

      if (columna == 9):
          columna = 8

      huecos = 0

      for i in range(3):
        if (carton[int(i)][int(columna)] == 0):
          huecos = huecos + 1
        if (carton[int(i)][int(columna)] == numero):
          huecos = 0
          break

      if (huecos < 2):
        continue

      fila = 0

      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1
        if (huecos < 5 or carton[int(fila)][int(i)] != 0):
          fila = fila + 1
        else:
          break

      if (fila == 3):
        continue

      carton[int(fila)][int(columna)] = numero
      numerosCarton = numerosCarton + 1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()

    return carton




def imprimirCarton(carton):
    for columna in range(3):
        for fila in range(9):
                print(carton[columna][fila])
        print('\n')




def no_mas_de_2_celdas_ocup_consec_x_fila(mi_carton):
    contador2 = 0
    contador1 = 0
    contador = 0
    aux = 0

    for contador in range(0, 3):
        for contador1 in range(0, 7):
            if (mi_carton[contador][contador1] > 0 and mi_carton[contador][contador1+1] > 0 and mi_carton[contador][contador1+2] > 0):
                contador2 += 1
        if contador2 != 0:
            aux = 1
    return (aux == 0)




def solo_3_colum_con_1_celda_ocup(mi_carton):
    contador = 0
    contador2 = 9
    aux = 0

    for i in range(contador2):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) == 1:
            contador += 1

        if contador != 3:
            aux = 1
    return (aux == 0)




def gdes_abajo_ch_arriba(mi_carton):
    contador = 0
    contador1 = 0
    aux = 0

    for contador in range(0,9):
        if mi_carton[0][contador] < mi_carton[1][contador] and mi_carton[1][contador] < mi_carton[2][contador]:
            contador1 += 1

    if contador1 != 9:
        aux = 1

    return (aux == 0)




def aumentan_de_izq_a_der(mi_carton):
    contador = 0
    contador1 = 0
    aux = 0

    for contador in range(0, 3):
        for contador1 in range(0, 8):
            if mi_carton[contador][contador1] != 0 and mi_carton[contador][contador1+1] != 0:
                if (mi_carton[contador][contador1] > mi_carton[contador][contador1+1]):
			aux = 1
    return (aux == 0)




def no_todas_las_celdas_de_column_ocup(mi_carton):
    contador = 0
    contador2 = 9
    aux = 0

    for i in range(contador2):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) < 3:
            contador += 1

    if contador != 9:
	aux = 1
    return(aux == 0)




def no_celdas_repetidas(mi_carton):
    contador = 0
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    aux = 0

    for contador1 in range(0, 3):
        for contador2 in range(0, 9):
                for contador3 in range(contador1, 3):
                    for contador4 in range(contador2, 9):
                        if mi_carton[contador1][contador2] == mi_carton[contador3][contador4]:
                            if mi_carton[contador1][contador2] != 0:
                                contador += 1
        if contador != 15:
            aux = 1
    return (aux == 0)




def sin_mas_de_2_celdas_vacias_consec_x_fila(mi_carton):
    contador2 = 0
    contador1 = 0
    contador = 0
    aux = 0

    for contador in range(0, 3):
        for contador1 in range(0, 7):
            if (mi_carton[contador][contador1] == 0 and mi_carton[contador][contador1+1] == 0 and mi_carton[contador][contador1+2] == 0):
                contador2 += 1
    if contador2 != 0:
        aux = 1
    return(aux == 0)




def sin_filas_vacias(mi_carton):
    contador = 3
    aux = 0

    for i in range(contador):
        if (mi_carton[i][0] + mi_carton[i][1] + mi_carton[i][2] + mi_carton[i][3] + mi_carton[i][4] + mi_carton[i][5] + mi_carton[i][6] + mi_carton[i][7] + mi_carton[i][8]) == 0:
            aux += 1
        
    return (aux == 0)




def x_fila_5_celdas_ocup(mi_carton):
    contador = 0

    for fila in range(3):
        aux = 0
        for columna in range(9):
            if mi_carton[fila][columna] > 0:
                contador += 1
                if contador != 3:
                    aux = 1
    return (aux == 0)




def no_columnas_vacias(mi_carton):
    contador = 0
    contador2 = 9

    for i in range(contador2):
        aux = 0
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) >= 1:
            contador += 1

        if contador != contador2:
            aux = 1
    return (aux == 0)




def nros_del_1_al_90(mi_carton):
   
    aux = 0

    for fila in range(0, 3):
        for columna in range(0, 9):
            celda = mi_carton[fila][columna]
            if celda >= 0 and celda <= 90:
                aux = 1
    return (aux==0)




def contar_celdas_ocupadas(mi_carton):
    celdas_ocupadas = 0
    aux = 0

    for fila in carton:
        for celda in fila:
            if celda != 0:
                celdas_ocupadas = celdas_ocupadas + 1
        if celdas_ocupadas != 15:
            aux = 1
    return (aux == 0)




def carton_9x3(mi_carton):
    aux=0

    if len(mi_carton) != 3:
        aux=1
    if len(mi_carton[0]) != 9:
        aux=1
    if len(mi_carton[1]) != 9:
        aux=1
    if len(mi_carton[2]) != 9:
        aux=1

    return (aux==0)

def generador_carton():
    auxx=0
    cant_cartones_inv=0
    while(auxx==0):
        mi_carton = intentoCarton()
        cant_cartones_inv = cant_cartones_inv + 1
        if(no_mas_de_2_celdas_ocup_consec_x_fila(mi_carton) == True
        and
        solo_3_colum_con_1_celda_ocup(mi_carton) == True
        and
        gdes_abajo_ch_arriba(mi_carton)== True
        and
        aumentan_de_izq_a_der(mi_carton)== True
        and
        no_todas_las_celdas_de_column_ocup(mi_carton)== True
        and
        no_celdas_repetidas(mi_carton) == True
        and
        sin_mas_de_2_celdas_vacias_consec_x_fila(mi_carton) == True
        and
        sin_filas_vacias(mi_carton) == True
        and
        x_fila_5_celdas_ocup(mi_carton) == True
        and
        no_columnas_vacias(mi_carton) == True
        and
        nros_del_1_al_90(mi_carton) == True
        and
        contar_celdas_ocupadas(mi_carton)== True
        and
        carton_9x3(mi_carton) == True):
                auxx=1
                print('\n')
                print('Antes de conseguir el carton correcto se intento la siguiente cant de veces:',cant_cartones_inv-1)
                print('\n')
    return mi_carton

carton = generador_carton()
imprimirCarton(carton)

