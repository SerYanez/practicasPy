# crear un menú con las siguientes opciones:
#
# Saludar
# Mostrar fecha
# Salir

while True:
    print("Qué quiere hacer hoy?")
    print("1- Saludar\n"
          "2- Mostrar fecha\n"
          "3- Salir")

    eleccion = input("Ingrese la opción elegida (1, 2, 3): ")
    match eleccion:
        case "1":
            print("Hola\n" * 100)
        case "2":
            print("La fecha de hoy es: hoy")
        case "3":
            print("Chau gato")
            exit()
        case _:
            print("ERRORRRREROORORERREOERROREROREOROORREEO")
