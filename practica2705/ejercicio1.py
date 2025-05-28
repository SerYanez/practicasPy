# Ejercicio 1: desarrollar un programa en Python que recorra los números del 1 al 9.
# Se deben mostrar únicamente los números impares y detenerse si se alcanza el número 7,
# sin incluirlo en la salida.

for numero in range (1,10):
    if numero % 2 == 0 :
        continue
    elif numero == 7 :
        break
    else:
        print(numero)