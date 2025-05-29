# Diseñar un algoritmo e implementarlo en Python que genere una lista de números
# del 1 al 20 utilizando un bucle. A partir de esta, generar una lista que contenga los
# números que sean pares y otra que contenga los números que sean impares.
# Mostrarlas en pantalla junto con el total de elementos de cada una.

''' Pseudocódigo

    CREAR una lista vacía para impares y otra para pares
    POR cada número en un rango de 20
        SI el número es par
            AGREGAR a lista par
        SI el número es impar
            AGREGAR a la lista impar
    MOSTRAR ambas listas
'''
impares = []
pares = []
for i in range(1,21):
        if i % 2 == 0:
            pares.append(i)
        elif i % 2 != 0:
            impares.append(i)

print(impares)
print(pares)
