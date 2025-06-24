# Dado el archivo calidad_de_agua.txt con las columnas: fecha y hora, caudal (m³/s)
# y temperatura promedio (°C) —columnas separadas por coma—, desarrollar un
# programa que:
# - Reemplace las comas por tabulaciones (\t),
# - Cambie los puntos decimales por comas,
# - Muestre el contenido resultante con los nombres de las columnas.

try:
    with open("calidad_de_agua.txt", "r+") as archivo:
        contenido = archivo.read()
        contenido = contenido.replace(",", "\t\t\t")
        contenido = contenido.replace(" ", "\t")
        contenido = contenido.replace(".", ",")
    columnas = ["Fecha", "Hora", "Caudal (m³/s)", "Temperatura promedio (°C)"]
    for elemento in columnas:
        print(elemento, end="\t\t")
    print()
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")
