# crear una función que reciba una lista de números y devuelva la media.
# Verificar que la lista no esté vacía y que contenga solo números.

def promedio(lista):
    if lista:
        try:
            return sum(lista) / len(lista)
        except TypeError:
            return "La lista contiene elementos que no son números."

notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
abc = ["a", "b", "c"]
aleatoria = [45, "asd", 9893, "xlcvkn", 213.2]

print(promedio(notas))
print(promedio(abc))
print(promedio(aleatoria))