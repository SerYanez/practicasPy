# Crear una función que permita repetir una palabra o carácter la cantidad de veces que el
# usuario decida e imprima el resultado.

def repetir(palabra, cantidad):
    print(palabra*cantidad)

palabra = input("Qué palabra desear repetir? ")
cantidad = int(input("Cuántas veces? "))

repetir(palabra, cantidad)