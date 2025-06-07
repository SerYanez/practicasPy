# Crear una función que reciba dos números ingresados por el usuario y
# devuelva la suma. Validar que ambos sean numéricos con try-except.

def sumar(nro1, nro2):
    total = nro1 + nro2
    return total

try:
    nro1 = float(input("Ingrese el primer número a sumar: "))
    nro2 = float(input("Ingrese el segundo número a sumar: "))
    print(sumar(nro1, nro2))
except ValueError:
    print("Debe ingresar un número.")