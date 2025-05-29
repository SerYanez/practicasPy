# Elaborar un programa en Python que permita mostrar los elementos de una
# matriz en formato tabla utilizando bucles (presentando una fila por línea).
# Luego, calcular la traza de la misma (la suma de los elementos de la diagonal
# principal y mostrar el resultado por pantalla.
# Matriz ejemplo: M = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

''' Pseudocódigo

    POR cada fila de la matriz
        POR cada elemento de la fila
            MOSTRAR el elemento seguido de un espacio
    CREAR variable traza valor 0
    POR cada elemento de la matriz
        SUMAR el elemento correspondiente al número de lista dentro de la matriz

'''

M = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

for i in M:
    for j in i:
        print(j, end=" ")
    print()
traza = 0
for i in range(len(M)):
    traza += M[i][i]
print(f"El valor de la traza es: {traza}")