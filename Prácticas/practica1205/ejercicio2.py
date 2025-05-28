# Desarrollar un pseudocódigo y codificar un programa que elimina duplicados de
# una lista de sílabas. Luego generar una tupla con las sílabas ordenadas
# alfabéticamente en orden inverso:
silabas = ["ba", "be", "bi", "ba", "bo", "bu", "be"]
silabas_unicas = set(silabas)
silabas_ordenadas = tuple(sorted(silabas_unicas, reverse=True))
print(silabas_ordenadas)