# Desarrollar un programa en Python que recorra un diccionario cuyas claves
# son nombres de estudiantes y cuyos valores son sus calificaciones (números
# del 1 al 10). El programa debe imprimir el nombre de cada estudiante, su
# calificación y un mensaje que indique si aprobó o desaprobó. Se considera
# aprobado si la nota es mayor o igual a 6.
# # Diccionario con estudiantes y sus notas
# notas = {
#  "Ana": 8,
#  "Luis": 5,
#  "Sofía": 9,
#  "Carlos": 4,
#  "Martina": 6
# }

'''

'''

notas = {
 "Ana": 8,
 "Luis": 5,
 "Sofía": 9,
 "Carlos": 4,
 "Martina": 6
}

for i, j in notas.items():
    if j < 6:
        print(f"{i} está desaprobado/a")
    elif j >= 6:
        print(f"{i} está aprobado/a")