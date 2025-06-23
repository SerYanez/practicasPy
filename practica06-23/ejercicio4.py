# Leer el contenido de un archivo llamado mediciones.txt utilizando readlines().
# Reemplazar los puntos decimales por comas en los valores numéricos, y guardar
# el resultado en un nuevo archivo llamado mediciones_modificadas.txt. Verificar
# previamente si el archivo existe.

def modif(file, nuevo_archivo):
    with open(file, "r") as archivo:
        lineas = archivo.readlines()
    with open(nuevo_archivo, "w") as nuevo:
        for i in lineas:
            linea = i.replace(".", ",")
            nuevo.write(linea)

with open("mediciones.txt", "r") as archivo:
    print(archivo.read())

modif("mediciones.txt", "mediciones_modificadas.txt")

with open("mediciones_modificadas.txt", "r") as archivo:
    print(archivo.read())