# Pedir al usuario que ingrese su edad. Si no es un número entero positivo,
# mostrar un mensaje y volver a pedirlo hasta que sea válido. Para todo usar
# una función leer_edad().

def leer_edad():
    while True:
        try:
            edad_input = int(input("Ingrese su edad: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue
        if not edad_input > 0:
            print("Edad inválida")
            continue
        else:
            print("Edad válida.")
            break

leer_edad()