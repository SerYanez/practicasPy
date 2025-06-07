# Implementar una función en Python que convierta las palabras de una lista dada a mayúsculas.
# ¿Es necesario usar la palabra global dentro de la función? ¿Por qué?

def convertir_a_mayus(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
        print(lista)

lista = ["hola", "loca"]
convertir_a_mayus(lista)