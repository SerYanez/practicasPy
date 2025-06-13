# crear una función que solicite al usuario ingresar un número entero positivo.
# Debe controlar que no se ingresen valores negativos ni texto no numérico.

def validar_num():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num >= 0:
            return num
        else:
            return "El número debe ser positivo."
    except ValueError:
        return "Debe ingresar un número entero válido."

print(validar_num())