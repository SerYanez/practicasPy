# Desarrollar un programa en Python que solicite al usuario ingresar un número
# entero positivo n y, utilizando un bucle, imprima un patrón de asteriscos en
# forma de triángulo rectángulo. Cada línea del patrón debe contener una
# cantidad de asteriscos igual al número de línea, comenzando con uno y
# aumentando hasta n. Ejemplo: para n = 4

''' Pseudocódigo

    ALMACENAR número entero ingresado por usuario en una variable
    POR el rango dado por la variable
        MOSTRAR "*" sumando 1 en cada iteración
'''

numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    print("*" * i)