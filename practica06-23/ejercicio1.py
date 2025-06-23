# Abrir un archivo llamado texto.txt, leer su contenido completo y mostrarlo por
# pantalla.

with open("texto.txt", "r") as archivo:
    cont = archivo.read()
    print(cont)