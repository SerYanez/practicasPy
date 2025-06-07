# Crear una función leer_entero(mensaje) que siga pidiendo hasta que el usuario
# ingrese un número válido. Usarla para construir programas más seguros.

def leer_entero(mensaje):
    while True:
        try:
            mensaje = int(input(mensaje))
            return mensaje
        except ValueError:
            print("Lo ingresado no es un número entero.")

num = leer_entero("Ingrese un número entero: ")
print(num)