# Implementar un menú de operaciones: suma, resta, multiplicación, división.
# Pedir dos números y operar según elección. Validar entrada y evitar división
# por cero.

def suma(nro1, nro2):
    return nro1 + nro2

def resta(nro1, nro2):
    return nro1 - nro2

def division(nro1, nro2):
    try:
        return nro1 / nro2
    except ZeroDivisionError:
        return "No se puede dividir por 0."

def multiplicacion(nro1, nro2):
    return nro1 * nro2

while True:
    print("Operaciones disponibles:\n"
          "1- Suma\n"
          "2- Resta\n"
          "3- División\n"
          "4- Multiplicación")
    eleccion = input("Ingrese la operación deseada: ").strip().lower().replace("ó", "o")
    if eleccion == "1" or eleccion == "suma":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese un número para sumar al primero: "))
            print(f"El resultado es: {suma(num_1, num_2):.2f}")
        except ValueError:
            print("Número inválido.")
    elif eleccion == "2" or eleccion == "resta":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese un número para restar al primero: "))
            print(f"El resultado es: {resta(num_1, num_2)}")
        except ValueError:
            print("Número inválido.")
    elif eleccion == "3" or eleccion == "division":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese un número para dividir por el primero: "))
            print(f"El resultado es: {division(num_1, num_2)}")
        except ValueError:
            print("Número inválido.")
    elif eleccion == "4" or eleccion == "multiplicacion":
        try:
            num_1 = float(input("Ingrese un número: "))
            num_2 = float(input("Ingrese un número para multiplicar por el primero: "))
            print(f"El resultado es: {multiplicacion(num_1, num_2)}")
        except ValueError:
            print("Número inválido.")
    else:
        print("Opción inválida.")
