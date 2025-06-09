# Leer 5 notas válidas (entre 0 y 10). Guardarlas en una lista. Calcular el
# promedio con una función. Validar tipo y rango de los datos ingresados.

def promedio(lista):
    if lista:
        promedio = sum(lista) / len(lista)
        return promedio
    else:
        print("La lista está vacía")

notas_lista = []

for i in range(5):
    while True:
        try:
            nota = float(input("Ingrese una nota(entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas_lista.append(nota)
                break
            else:
                print("La nota debe ser entre 0 y 10")
        except ValueError:
            print("No es un número.")

print(f"Hay {len(notas_lista)} notas registradas.")
print("El promedio de notas es: ", promedio(notas_lista))