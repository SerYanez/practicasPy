#4- A partir de la lista de tuplas pares = [("a", 1), ("b", 2), ("c", 3)], convertirla en
#un diccionario y acceder al valor asociado a la clave "b".

pares = [("a", 1), ("b", 2), ("c", 3)]

mi_dic = dict(pares)
print(mi_dic["b"])