# Crear un diccionario llamado operaciones_matematicas donde las claves sean strings que
# representen operaciones (por ejemplo: suma, resta, multiplicacion, division), y los valores
# sean funciones que realicen las operaciones entre dos números.
# Luego, solicitar al usuario que ingrese dos números y el tipo de operación que desea realizar.
# Utilizar el diccionario para invocar la función correspondiente y mostrar el resultado

def sumar(nro_1, nro_2):
    return nro_1 + nro_2

def restar(nro_1, nro_2):
    return nro_1 - nro_2

def dividir(nro_1, nro_2):
    if nro_2 == 0:
        return "No se puede hacer división por 0"
    else:
        return nro_1 / nro_2

def multiplicar(nro_1, nro_2):
    return nro_1 * nro_2

operaciones_matematicas = {
    "suma" : sumar,
    "resta" : restar,
    "división" : dividir,
    "multiplicación" : multiplicar
}


nro_1 = float(input("Ingrese el primer nro: "))
nro_2 = float(input("Ingrese el segundo nro: "))
operacion = input("Ingrese la operación a realizar (suma, resta, división, "
                  "multiplicación): ").lower().strip().replace("o", "ó")

if operacion in operaciones_matematicas:
    eleccion = operaciones_matematicas[operacion]
    resultado = eleccion(nro_1, nro_2)
    print(f"Resultado: ", resultado)
else:
    print("Operación inválida.")