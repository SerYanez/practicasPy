# Se tiene un archivo binario llamado mensaje.bin, el cual contiene un mensaje
# codificado como una cadena binaria. Cada 8 bits representan un carácter
# codificado en UTF-8. Escribir un programa en Python que muestre el mensaje
# original por pantalla.

try:
    with open("mensaje.bin", "rb") as archivo:
        contenido = archivo.read()
    print(contenido)
    mensaje = ""
    for bit in range(0, len(contenido), 8):
        byte = contenido[bit:bit+8]
        letra = chr(int(byte, 2))
        mensaje += letra
    print(mensaje)
except FileNotFoundError:
    print("archivo inexistente.")
except UnicodeError:
    print("error al decodificar")