# Leer un archivo llamado documento.txt línea por línea y contar cuántas líneas
# contiene. Mostrar el total obtenido por pantalla.

def contar_lineas(archivo):
    contador = 0
    with open(archivo, "r") as file:
        for i in file:
            contador += 1
    return contador

print(contar_lineas("documento.txt"))