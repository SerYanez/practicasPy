#2- Crear un diccionario alumno con claves: nombre, materias (lista de 3
# materias), y edad.
# a- Solicitar al usuario los datos del alumno,
# b- Asignar una lista de 3 materias a la clave materias,
# c- Agregar una materia a la lista y verificar si "Matemática" está entre
# sus materias.

alumno = {"Nombre" : "", "Materias" : [], "Edad" : 0}

nombre = input("Ingrese nombre del estudiante: ")
materia_1 = input("Ingrese 1er materia que cursa: ")
materia_2 = input("Ingrese 2da materia que cursa: ")
materia_3 = input("Ingrese 3er materia que cursa: ")
edad = input("Edad del estudiante: ")
listado_materias = [materia_1, materia_2, materia_3]

alumno ["Nombre"] = nombre
alumno ["Materias"] = listado_materias
alumno ["Edad"] = edad

materia_4 = input("Agregue una 4ta materia: ")
listado_materias.append(materia_4)

chequeo = "Matemática"
resultado = chequeo in listado_materias
print("Matemática es una de las materias? ", resultado)