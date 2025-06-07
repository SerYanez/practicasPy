# Crear una función que convierta grados Celsius a Fahrenheit. Controlar que el
# valor ingresado sea un número decimal válido.

def convertir_a_f():
    while True:
        try:
            temp = float(input("Ingrese una temperatura en celsius: "))
            farenheit = temp * 9/5 +32
            return farenheit
        except ValueError:
            return "Número inválido"

print(convertir_a_f())
