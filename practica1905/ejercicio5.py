#5- Crear un diccionario con tuplas como claves: usar coordenadas (latitud,
#longitud) como claves y nombres de ciudades como valores. Mostrar la
#ciudad asociada a una coordenada dada.

coordenadas = {}
coordenadas[(1, 2)] = "Paris"
coordenadas[(3, 4)] = "Roma"
coordenadas[(5, 6)] = "Berlín"
coordenadas[(7, 8)] = "Madrid"
coordenadas[(9, 10)] = "Zurich"

print("Consulte una ciudad a partir de sus coordenadas: ")
alt = int(input("Ingrese altitud: "))
lat = int(input("Ingrese latitud: "))
coor_ingresada = (alt, lat)

print("La ciudad es: ", coordenadas[coor_ingresada])