# Pedir al usuario que ingrese por teclado 3 notas y guardarlas en una lista.
# Crear una función calcular_promedio(lista_notas) que devuelva el promedio.
# Mostrar si el estudiante aprobó (promedio ≥ 6) o no. ¿Qué variables globales y qué
# variables locales se utilizan en este programa?

def calcular_promedio(lista_notas):
    suma = sum(lista_notas)
    promedio = float(suma / 3)
    print(f"Promedio de notas: ", round(promedio, 2))
    return round(promedio, 2)

lista_notas = []
print("Ingrese sus notas: ")
nota_1 = input("Nota 1: ")
lista_notas.append(float(nota_1))
nota_2 = input("Nota 2: ")
lista_notas.append(float(nota_2))
nota_3 = input("Nota 3: ")
lista_notas.append(float(nota_3))

if calcular_promedio(lista_notas) >= 6:
    print("Aprobado")
else:
    print("desaprobado")