while True:
    entrada = input("Ingrese un nro entero: ")
    try:
        nro = int(entrada)
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

if nro == 2:
    print("El nro ingresado es 2")
elif nro > 0:
    (print("El nro es mayor a 0"))
elif nro < 0:
    print("El nro es menor a 0")
else:
    print("El nro ingresado no es 2")

if nro % 2 == 0:
    print("El nro es par")
else:
    print("El nro es impar")

print("Fin del programa")