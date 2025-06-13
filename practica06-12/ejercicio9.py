# Crear una función que solicite un ingreso de número entero. Si es válido y par,
# informar al usuario

def ingreso_num():
    try:
        num = int(input("Ingrese un número entero: "))
        if num % 2 == 0:
            return "El número es válido y par"
        else:
            return "El número es válido pero impar"
    except ValueError:
        return "No ingresó un número válido."

print(ingreso_num())