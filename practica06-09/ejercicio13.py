# Pedir al usuario que ingrese una operación matemática como texto ("3 + 5").
# Usar eval() con try-except para ejecutar la operación de forma controlada


ingreso = input("Ingrese una operación que desee realizar: ")
try:
    print(eval(ingreso))
except SyntaxError:
    print("Operación inválida.")
except ZeroDivisionError:
    print("No se puede dividir por 0.")
except NameError:
    print("Debe ingresar operaciones matemáticas válidas.")