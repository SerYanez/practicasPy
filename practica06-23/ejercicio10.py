# Intentar abrir un archivo llamado config.txt. En caso de que no exista, mostrar un
# mensaje en pantalla e inmediatamente crearlo con contenido por defecto que
# incluya tres líneas de configuración (clave=valor)

try:
    with open("config.txt", "r") as archivo:
        contenido = archivo.read()
        print("Archivo existente!")
        print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado! Creando...")
    with open("config.txt", "w") as archivo:
        archivo.write(str({"Clave_1" : "valor"}))
        archivo.write(str({"Clave_2": "valor"}))
        archivo.write(str({"Clave_3": "valor"}))