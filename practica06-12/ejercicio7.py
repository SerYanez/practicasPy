# crear una función que reciba una lista de elementos e intente acceder a un índice ingresado
# por el usuario.

# búsqueda por elemento
"""def busqueda_elemento(lista):
    elemento = input("Ingrese el elemento que desea buscar en la lista: ")
    encontrado = False
    for i in lista:
        if i == elemento or i == float(elemento):
            encontrado = True
    if encontrado == True:
        print(f"El elemento '{elemento}' está en la lista")
    else:
        print("El elemento no está en la lista.")"""

def mostrar_elemento(lista):
    try:
        elemento = int(input("Ingrese un número de índice para mostrar de la lista: "))
        if elemento == 0:
            return f"El último elemento de la lista es: {lista[elemento -1]}"
        return lista[elemento - 1]
    except IndexError:
        return f"No existe el elemento '{elemento}' en la lista"
    except ValueError:
        return "Debe ingresar un número entero para buscar por índice en la lista."

etc = ["ola", 45, "hola", 21, "onda", 99]

print(mostrar_elemento(etc))