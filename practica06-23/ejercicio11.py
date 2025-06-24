# Dado un archivo invitacion.txt con los marcadores [DESTINATARIO] y
# [REMITENTE], solicitar al usuario el nombre del destinatario y el del remitente,
# reemplazar esos marcadores en el texto, y mostrar la invitación personalizada por
# pantalla.

def personalizacion(file, destinatario, remitente):
    try:
        with open(file, "r+", encoding="utf-8") as archivo:
            contenido = archivo.read()
            contenido = contenido.replace("[DESTINATARIO]", destinatario)
            contenido = contenido.replace("[REMITENTE]", remitente)
        return contenido
    except FileNotFoundError:
        return "El archivo no existe."

nombre_dest = input("Ingrese el nombre del destinatario: ")
nombre_rem = input("Ingrese el nombre del remitente: ")
archivo = input("Ingrese el nombre del archivo a modificar: ")

print(personalizacion(archivo, nombre_dest, nombre_rem))