# Escribir una función que reciba un número y devuelva su factorial.

def factorial(numero):
    for i in range(1,numero):
        numero *= i
    return numero

numero = int(input("Ingrese un número: "))
print(factorial(numero))
