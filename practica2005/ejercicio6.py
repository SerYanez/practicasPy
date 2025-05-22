#se explica qué hace el programa
print("Este programa muestra la mitad, "
      "el doble o el triple del número que usted ingrese")

#se pide ingresar una de las opciones y se guarda en una variable
eleccion = input(f"Elija una de las opciones: \na) Mitad\nb) Doble\nc) Triple\n")

#se pide ingresar un número para hacer la operación requerida y se lo guarda en una variable
nro = float(input("Ingrese un número: "))

# se compara la elección de operación con las posibilidades,
# y se realiza la requerida sobre el número ingresado.
# también se intenta reducir lo más posible la posibilidad de error de entrada

match eleccion.strip().lower():
      case "a) mitad" | "a)" | "mitad" | "a" :
            print("El resultado es: ", nro / 2)
      case "b) doble" | "b)" | "doble" | "b":
            print("El resultado es: ", nro * 2)
      case "c) triple" | "c)" | "triple" | "c":
            print("El resultado es: ", nro * 3)
      case _ : print("Opción no válida")
