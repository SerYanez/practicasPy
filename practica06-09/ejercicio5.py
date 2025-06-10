# Crear una función que convierta grados Celsius a Fahrenheit. Controlar que el
# valor ingresado sea un número decimal válido.

def convertir_a_f(temp):
    try:
        temp = float(temp)
        farenheit = temp * 9/5 + 32
        return farenheit
    except ValueError:
        return "Número inválido"

celsius = input("Ingrese una temperatura en celsius: ")
print(convertir_a_f(celsius))
