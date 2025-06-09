# Implementar una función que reciba dos números y devuelva su cociente.
def dividir(nro1, nro2):
    return nro1 / nro2

while True:
    try:
        nro1 = float(input("Ingrese el dividendo: "))
        nro2 = float(input("Ingrese el divisor: "))
        print(dividir(nro1, nro2))
        break
    except ValueError:
        print("Debe ingresar un número.")
    except ZeroDivisionError:
        print("El número ingresado debe ser mayor a 0")