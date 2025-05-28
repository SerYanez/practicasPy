#Crear un diccionario a partir de un set de nombres y una lista de edades,
#asegurando el orden. Convertir el set a lista y luego combinar con zip() y
#dict().

nombres = {"Ana", "Pedro", "Lucía"} # set sin orden garantizado
edades = [25, 30, 22] # lista con orden definido

nombres_lista = sorted(nombres)
print(nombres_lista)
alumnos = dict(zip(nombres_lista, edades))

print(alumnos)