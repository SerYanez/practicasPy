# Ejercicio 3: desarrollar un algoritmo que permita agregar datos a la lista.

''' Pseudocódigo
#INICIO
    MIENTRAS el usuario quiera continuar en el programa
        INGRESAR si quiere agregar datos, ALMACENANDO respuesta en una variable
        SI la respuesta es positiva:
            INGRESAR datos, almacenando cada uno en variables
            CREAR un diccionario con claves correspondientes,
            de valor cada variable almacenada anteriormente
            AGREGAR diccionario a lista de personas

        SI la respuesta es negativa:
            MIENTRAS continue en el menú:
                INGRESAR si quiere consultar datos almacenados
                    SI la respuesta es positiva:
                        MOSTRAR lista de personas
                    SI la respuesta es negativa:
                        MOSTRAR mensaje de despedida
                        SALIR del bucle
            SALIR del bucle, terminando el programa

        SI ingresa cualquier otra opción:
            MOSTRAR mensaje de opción inválida y se repite el bucle'''

personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Bahia Blanca"},
    {"nombre": "Luis", "edad": 17, "ciudad": "Cordoba"},
    {"nombre": "Sofía", "edad": 30, "ciudad": "Bahia Blanca"},
    {"nombre": "Carlos", "edad": 15, "ciudad": "Rosario"}
]



while True:
    opcion = input("Desea ingresar nuevos datos a la lista de personas? S/N:\n")

    if opcion.lower().strip() == "s":
        print("Ingrese datos a la lista de personas: ")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        ciudad = input("Ingrese la ciudad de residencia: ")
        persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
        personas.append(persona)

    elif opcion.lower().strip() == "n":
        while True:
            opcion = input("Desea ver la lista de personas? S/N")
            if opcion.lower().strip() == "s":
                print(personas)
            elif opcion.lower().strip() == "n":
                print("Gracias por usar el programa!")
                break
            else:
                print("Opción inválida, seleccione S o N")
        break

    else:
        print("Opción inválida, seleccione S o N")
