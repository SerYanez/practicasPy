# Crear una lista de elementos y pedir al usuario un valor para buscar. Controlar
# que la lista no esté vacía y que el dato exista.

def busqueda_lista(elemento, lista):
    if not lista:
        print("La lista está vacía.")
    if elemento in lista:
        print("El elemento se encuentra en esta lista.")
    else:
        print("El elemento no se encuentra en esta lista.")


abecedario = ["a", "b", "c", "d", "e"]
notas = [1, 5, 10, 8, 9]
ropa = []
gastos = [111.6, 125.5, 20.7]
otros = []

listas_disponibles = {
    "abecedario" : abecedario,
    "notas" : notas,
    "ropa" : ropa,
    "gastos" : gastos,
    "otros" : otros
}

entrada = input("Ingrese lo que desea buscar: ").strip()
try:
        elemento_a_buscar = float(entrada)
except ValueError:
    elemento_a_buscar = entrada.lower()

lista_ingresada = input("Ingrese el nombre de la lista donde buscar: ").strip().lower()
if lista_ingresada in listas_disponibles:
    lista_donde_buscar = listas_disponibles[lista_ingresada]
    busqueda_lista(elemento_a_buscar, lista_donde_buscar)
else:
    print("Lista no existente.")