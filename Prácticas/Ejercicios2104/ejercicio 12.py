nombre_uno = input("Ingrese su nombre: ")
nombre_dos = input("Ingréselo nuevamente: ")

comparacion_nombre = nombre_dos.lower() == nombre_uno.lower()

print(f"Ingresó el mismo nombre? {comparacion_nombre}")