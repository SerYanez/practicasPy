# Abrir un archivo binario llamado texto.bin, que contiene un texto. Leer los primeros
# 10 bytes del archivo y mostrarlos uno por uno por pantalla
try:
    with open("texto.bin", "rb") as archivo:
        primeros_10 = archivo.read(10)
        contador = 1
        for byte in primeros_10:
            print(f"Byte {contador}: {byte}")
            contador += 1
except FileNotFoundError:
    print("El archivo no existe.")