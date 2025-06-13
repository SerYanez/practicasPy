# Crear una función para convertir una cadena de texto en un número entero.
# Si la conversión falla, mostrar mensaje de error y volver a pedir el valor.

def convertir_cadena(cadena_texto):
        try:
            cadena_convertida = int(cadena_texto)
            return cadena_convertida
        except ValueError:
            print("Debe ingresar un valor numérico.")
            return None

convertido = None
while convertido is None:
    cadena = input("Ingrese un valor numérico: ")
    convertido = convertir_cadena(cadena)

print(f"El número ingresado es: {convertido}")