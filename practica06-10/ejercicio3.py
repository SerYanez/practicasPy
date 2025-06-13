# Ejercicio 3: crear un programa que implemente un menú con estas opciones:
# 1. Calcular raíz cuadrada de un número
# 2. Dividir dos números
# 3. Calcular promedio de N notas
# 5. Salir

def raiz_cuadrada(num):
        return num ** 0.5

def dividir(nro1, nro2):
        return nro1 / nro2

def promedio(lista):
        return sum(lista) / len(lista)



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
opcion = ""

while not opcion == "4":
    print("Seleccione una operación a realizar:\n"
          "1- Raíz cuadrada\n"
          "2- División\n"
          "3- Promedio\n"
          "4- Salir\n")
    opcion = input("Ingrese la operación deseada: ").strip().lower().replace("ó", "o")
    if opcion == "1" or opcion == "raiz" or opcion == "raiz cuadrada":
        try:
            num = float(input("Ingrese un número: "))
            print(f"El resultado es: {raiz_cuadrada(num)}")
        except ValueError:
            print("Número inválido.")
    elif opcion == "2" or opcion == "division":
        try:
            num_1 = float(input("Ingrese el dividendo: "))
            num_2 = float(input("Ingrese el divisor: "))
            print(f"El resultado es: {dividir(num_1, num_2)}")
        except ValueError:
            print("Debe ingresar números válidos")
        except ZeroDivisionError:
            print("No se puede dividir por 0")
    elif opcion == "3" or opcion == "promedio":
        if lista:
            try:
                print(f"La lista contiene estas notas: {len(lista)}"
                      f"Las notas son: {lista}")
                print(promedio(lista))
            except ValueError:
                print("Debe ingresar una lista de números válidos")
            except TypeError:
                print("Debe ingresar una lista números válidos")
    elif opcion == "4" or opcion == "salir":
        print("Saliendo del programa")
    else:
        print("Opción inválida.")
