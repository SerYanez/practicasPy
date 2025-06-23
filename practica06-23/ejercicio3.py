# Permitir el ingreso de nuevas frases por parte del usuario y agregarlas al final de
# un archivo existente llamado frases.txt, sin borrar su contenido previo.

with open("frases.txt", "a") as archivo:
    archivo.write(input("Ingrese una nueva frase: "))