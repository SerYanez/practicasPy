# Permitir el ingreso de nuevas frases por parte del usuario y agregarlas al final de
# un archivo existente llamado frases.txt, sin borrar su contenido previo.

nueva_frase = input("Ingrese una nueva frase: ")

with open("frases.txt", "a") as archivo:
    archivo.write(nueva_frase)

print("El contenido actualizado del archivo es: \n")

with open("frases.txt", "r") as archivo:
    print(archivo.read())