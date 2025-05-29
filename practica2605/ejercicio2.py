# Diseñar e implementar un algoritmo en Python que calcule la sumatoria de los
# primeros N números naturales y muestre el resultado por pantalla.

''' Pseudocódigo
    CREAR variable suma en 0
    CREAR un bucle en un rango de 10, los primeros números naturales
        SUMAR el nro actual a la variable suma por cada iteración
        MOSTRAR resultado
'''

suma = 0
for i in range(1,11):
    suma += i
    print(suma)
