# Crear una función leer_entero(mensaje) que valide si el dato ingresado es un entero.

def leer_entero(mensaje):
    try:
        convertir = int(mensaje)
        return "El mensaje ingresado es un número entero"
    except ValueError:
        return "El mensaje ingresado no es un número entero."

mensaje = input("Ingrese un mensaje para comprobar si es un número entero: ")
print(leer_entero(mensaje))