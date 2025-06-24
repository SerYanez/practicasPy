# Leer el contenido del archivo original.txt, convertirlo a mayúsculas, y guardar el
# resultado en un archivo nuevo llamado mayusculas.txt.

with open("original.txt", "r") as archivo:
    contenido = archivo.read()

contenido_nuevo = contenido.upper()
with open("mayusculas.txt", "w") as archivo:
    archivo.write(contenido_nuevo)