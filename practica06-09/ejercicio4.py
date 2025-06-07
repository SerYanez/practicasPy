# Leer 5 notas válidas (entre 0 y 10). Guardarlas en una lista. Calcular el
# promedio con una función. Validar tipo y rango de los datos ingresados.

def promedio(lista):
    if lista:
        total = sum(lista)
        promedio = total / len(lista)
        return promedio
    else:
        print("La lista está vacía")

def validar_nro():
    while True:
        try:
            nota = float(input("Ingrese una nota(entre 0 y 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("La nota debe ser entre 0 y 10")
        except ValueError:
            print("No es un número.")

def mostrar_lista(lista):
    print("Las notas registradas son: ", end="")
    for i in lista:
        print(i, end=" ")
    print()

notas_lista = []

nota_1 = validar_nro()
print("Primer nota agregada a la lista")
notas_lista.append(nota_1)
nota_2 = validar_nro()
print("Segunda nota agregada a la lista")
notas_lista.append(nota_2)
nota_3 = validar_nro()
print("Tercer nota agregada a la lista")
notas_lista.append(nota_3)
nota_4 = validar_nro()
print("Cuarta nota agregada a la lista")
notas_lista.append(nota_4)
nota_5 = validar_nro()
print("Quinta nota agregada a la lista")
notas_lista.append(nota_5)

print(f"Hay {len(notas_lista)} notas registradas.")
mostrar_lista(notas_lista)
print("El promedio de notas es: ", promedio(notas_lista))