# Solicitar al usuario su nombre, edad y ciudad. Almacenar estos datos en un
# diccionario y guardar su contenido en un archivo denominado usuario.txt,
# escribiendo cada valor en una línea separada.

def almacenar_datos(archivo):
    datos = {"nombre": input("Ingrese su nombre: "), "edad": input("Ingrese su edad: "),
             "ciudad": input("Ingrese el nombre de la ciudad donde reside: ")}
    with open("usuario.txt", "w") as archivo:
        for clave, valor in datos.items():
            archivo.write(f"{clave}: {valor} \n")

almacenar_datos("usuario.txt")
with open("usuario.txt", "r") as archivo:
    print(archivo.read())