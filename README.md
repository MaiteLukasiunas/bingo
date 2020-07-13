# bingo

[![Coverage Status](https://coveralls.io/repos/github/MaiteLukasiunas/bingo/badge.svg?branch=master)](https://coveralls.io/github/MaiteLukasiunas/bingo?branch=master)

Proyecto para la materia Adaptacion del Ambiente De Trabajo del Instituto Politecnico Superior General San Martin del profesor Mariano Dagostino

###Objetivo:
  - Crear un programa que genere cartones de bingo y que corriendo una serie de tests descarte aquellos que no sean validos y muestre el carton valido conseguido.

### Los tests que deben cumplirse para lograr un carton valido son:
  - Los números del cartón se encuentran en el rango 1 a 90.
  - Cada columna de un cartón (contando de izquierda a derecha) contiene números que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
  - No hay números repetidos en el cartón.
  - Cada fila de un cartón tiene exactamente 5 celdas ocupadas.
  - Cada cartón es una matriz de 3 x 9.
  - Cada cartón tiene 15 celdas ocupadas.
  - Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
  - Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
  - No pueden existir columnas vacías.
  - No pueden existir columnas con sus tres celdas ocupadas.
  - Cada cartón debe tener 3 y solo 3 columnas con solo una celda ocupada.
  - En una fila no existen más de dos celdas vacías consecutivas.
  - En una fila no existen más de dos celdas ocupadas consecutivas.
