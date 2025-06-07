# Pedir nombre y edad de varias personas. Validar que la edad sea un entero
# positivo. Guardar en una lista de diccionarios. Finalizar al escribir “fin”

lista_personas = []
while True:
    print("Ingrese 1 para registrar los datos de una persona en la lista\n"
          "Ingrese 2 para ver los datos registrados\n"
          "Ingrese 'FIN' para salir")
    eleccion = input("").strip().lower()
    if eleccion == "1":
        nombre = input("Ingrese el nombre de una persona: ")
        try:
            edad = int(input("Ingrese la edad de la persona: "))
            if not 125 < edad < 0:
                persona = {nombre : edad}
                lista_personas.append(persona)
                print("Persona agregada a la lista.")
            else:
                print("Edad inválida")
        except ValueError:
            print("La edad debe ser un número entero.")
    elif eleccion == "2":
        if lista_personas:
            print("Personas registradas: ")
            for i in lista_personas:
                 print(i)
        else:
            print("No hay personas registradas.")
    elif eleccion == "fin":
        print("Hasta luego.")
        exit()
    else:
        print("Opción inválida.")