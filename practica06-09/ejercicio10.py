# Desarrollar una función que calcule el factorial de un número ingresado. Validar
# que sea un entero positivo. Capturar errores si el dato no es válido.

def factorial(numero):
    resultado = 1
    for i in range(1,numero + 1):
        resultado *= i
    return resultado

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero >= 0:
            print(f"El factorial de {numero}, es {factorial(numero)}")
        else:
            print("El número debe ser positivo o 0")
    except ValueError:
        print("Dato inválido, debe ser un número entero.")