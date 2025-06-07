# Elaborar un programa en Python que, a partir de una lista dada de palabras,
# convierta cada una de ellas a mayúsculas (sobre la misma lista) utilizando un bucle.
# Al finalizar el proceso, se debe mostrar por pantalla la lista resultante

''' Pseudocódigo

    POR cada elemento de la lista
        CONVERTIR el elemento a mayúsculas
        MOSTRAR lista
'''

palabras = ["Almohada", "Tormenta", "Eclipse", "Martillo", "Jardín", "Nebulosa",
"Cuadro", "Delfín", "Caverna", "Relámpago"]

for i in range(len(palabras)):
    palabras[i] = palabras[i].upper()
    print(palabras)