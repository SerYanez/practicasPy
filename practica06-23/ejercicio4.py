# Leer el contenido de un archivo llamado mediciones.txt utilizando readlines().
# Reemplazar los puntos decimales por comas en los valores numéricos, y guardar
# el resultado en un nuevo archivo llamado mediciones_modificadas.txt. Verificar
# previamente si el archivo existe.

def modif(file, nuevo_archivo):
    try:
        with open(file, "r") as archivo:
            lineas = archivo.readlines()
        try:
            with open(nuevo_archivo, "x") as nuevo:
                for i in lineas:
                    linea = i.replace(".", ",")
                    nuevo.write(linea)
                return nuevo.read()
        except FileExistsError:
            return "El archivo modificado ya existe."
    except FileNotFoundError:
        return f"El archivo {file} no existe."

with open("mediciones.txt", "r") as archivo:
    print(archivo.read())

print(modif("mediciones.txt", "mediciones_modificadas.txt"))