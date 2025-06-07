# Diseñar una función mostrar_numeros_pares(hasta_numero) que muestre los números pares desde
# 1 hasta el número que haya indicado el usuario. Se debe validar dentro de la función que el
# número sea mayor que cero.

def mostrar_numeros_pares(hasta_numero):
    if hasta_numero > 0:
        for i in range(1, hasta_numero + 1):
            if i % 2 == 0:
                print(i)
    else:
        exit()

hasta_numero = int(input("Ingrese un número entero: "))
mostrar_numeros_pares(hasta_numero)