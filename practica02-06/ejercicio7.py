# Elaborar un código en Python que implemente una función que reciba una lista de edades
# y devuelva la edad mínima, la máxima y el promedio. Los datos se ingresan por teclado hasta
# que el usuario escriba "fin".


def datos_lista(edades):
    if not edades:
        return "La lista está vacía"
    edad_min = min(edades)
    edad_max = max(edades)
    promedio = sum(edades) / len(edades)
    return edad_min, edad_max, promedio

lista_edades = []

while True:
    eleccion = input("Quiere agregar una edad a la lista? S/N: ").lower().strip()
    if eleccion == "s":
        try:
            edad = int(input("Ingrese una edad: "))
            print("La edad ha sido ingresada")
            lista_edades.append(edad)
        except ValueError:
            print("Edad inválida.")
    elif eleccion == "n":
        seleccion = input("Quiere ver los datos de la lista? S/N: ").lower().strip()
        if seleccion == "s":
            print(datos_lista(lista_edades))
        elif seleccion == "n":
            print("Gracias, hasta luego.")
            break
    else:
        print("Elección inválida, intente nuevamente.")