op = int(input("ingrese 1, 2 o 3: "))

match op:
  case 1:
    print("usted eligio la opción 1")
  case 2:
    print("usted eligio la opción 2")
  case 3:
    print("usted eligio la opción 3")
  case _:
    print("usted eligio una opción inválida")