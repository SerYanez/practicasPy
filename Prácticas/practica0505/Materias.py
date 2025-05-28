#Crear una lista llamada materias con tres materias que cursás este
#cuatrimestre
materias = ["Matemática", "Python", "Comunicación"]
#a- Imprimir el segundo elemento
print(materias[1])
#b- Insertar una nueva materia en la posición 2
materias.insert(2,"Inglés")
print(materias)
#c- Agregar un elemento en la posición cero.
materias.insert(0,"Administración")
print(materias)
#d- Eliminar el elemento de la posición 1.
materias.pop(1)
print(materias)
#e- Ordenar la lista en orden inverso
materias.sort(reverse = True)
print(materias)