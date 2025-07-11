# Se tiene un archivo llamado datos_climaticos.txt con información meteorológica.
# La primera línea del archivo corresponde a los nombres de las columnas, mientras
# el resto de las líneas son datos numéricos correspondientes a cada columna.
# Desarrollar un programa en Python que lea el archivo y complete un diccionario
# donde las claves sean los encabezados, mientras que los valores serán los datos
# del resto de las filas. Finalmente, mostrar el diccionario en pantalla.

try:
    with open("datos_climaticos.txt", "r") as archivo:
        encabezados = archivo.readline().strip().split(",")
        datos = []
        for linea in archivo:
            fila = {}
            valores = linea.strip().split(",")
            for i in range(len(encabezados)):
                fila[encabezados[i]] = valores[i]
            datos.append(fila)
        for linea in datos:
            print(f"Fecha: {linea["fecha"]}, temperatura máxima: {linea["temperatura_max"]}, "
                  f"temperatura mínima: {linea["temperatura_min"]}, precipitación: {linea["precipitacion"]} ")
except FileNotFoundError:
    print("El archivo no existe")