#  pedir al usuario que ingrese 5 notas (números decimales). Guardarlas en una lista y mostrar:
#
# Todas las notas
#
# El promedio
#
# Si está aprobado (promedio ≥ 6) o no

notas_lista = []
nota_1 = float(input("Ingrese la primera nota: "))
notas_lista.append(nota_1)
nota_2 = float(input("Ingrese la segunda nota: "))
notas_lista.append(nota_2)
nota_3 = float(input("Ingrese la tercer nota: "))
notas_lista.append(nota_3)
nota_4 = float(input("Ingrese la cuarta nota: "))
notas_lista.append(nota_4)
nota_5 = float(input("Ingrese la quinta nota: "))
notas_lista.append(nota_5)

print("Notas registradas: ")
for i in notas_lista:
    print(i, end=" ")
print()
total_notas = sum(notas_lista)
promedio_notas = total_notas / len(notas_lista)
print(f"Promedio: {promedio_notas}")
if promedio_notas >= 6:
    print("Aprobado")
elif promedio_notas < 6:
    print("Desaprobado")