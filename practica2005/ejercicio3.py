#pido que el usuario ingrese un número
nro = int(input("Ingrese un número entero: "))

#hago el chequeo de si el nro es par o impar
if nro % 2 == 0:
    print("El nro ingresado es par")
else:
    print("El nro ingresado es impar")

#pido que el usuario ingrese otro nro
nro_dos = int(input("Ingrese otro número entero: "))

#hago el chequeo de si el nro es par o impar
if nro_dos % 2 == 0:
    print("El nro ingresado es par")
else:
    print("El nro ingresado es impar")

#comparo nro 1 con nro 2
if nro > nro_dos:
    print("El primer nro es mayor que el segundo")
elif nro < nro_dos:
    print("El segundo nro es mayor que el primero")
else:
    print("Los números son iguales")