# Dada una lista que contiene tuplas con horarios (hora, minuto), eliminar los
#horarios duplicados y ordenarlos de menor a mayor (previamente, elaborar el
#pseudocodigo).

horarios = [(8, 30), (9, 15), (8, 30), (10, 45), (9, 15)]

# INICIO
# utilizar la función sorted para ordenar el contenido del conjunto
# pasando de lista a set

horarios_limpio = sorted(set(horarios))
print(horarios_limpio)