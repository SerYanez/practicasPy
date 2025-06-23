# Pedir al usuario que ingrese una palabra. Verificar si dicha palabra se encuentra
# dentro del contenido de un archivo llamado noticias.txt. Informar el resultado por
# pantalla.

def encontrar_palabra(palabra, archivo):
    with open(archivo, "r") as archivo:
        for linea in archivo:
            if not palabra in linea:
                return "Palabra no encontrada."
            else:
                return "Palabra encontrada en el archivo."

print(encontrar_palabra("ministro", "noticias.txt"))