# crear una función que reciba dos números y devuelva su cociente.
# Controlar división por cero con try-except.
# ¿Se puede controlar de otra manera?

# R: Sí, se puede controlar a través de condicionales. Si el número es 0, no se llama a la función


def dividir(num1, num2):
    try:
        return f"El resultado es: {float(num1) / float(num2)}"
    except ValueError:
        return "Ha ingresado caracteres no numéricos."
    except ZeroDivisionError:
        return "No se puede hacer división por 0."

num_1 = input("Ingrese un dividendo: ").strip()
num_2 = input("Ingrese un divisor: ").strip()

print(dividir(num_1, num_2))