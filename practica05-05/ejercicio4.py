cadena_caracteres = input("Ingrese un texto para analizar: ")

vocales= [cadena_caracteres.count("a"), cadena_caracteres.count("e"), cadena_caracteres.count("i"),
          cadena_caracteres.count("o"), cadena_caracteres.count("u")]


print("Cantidad de veces que aparece la letra A: ", vocales[0])
print("Cantidad de veces que aparece la letra E: ", vocales[1])
print("Cantidad de veces que aparece la letra I: ", vocales[2])
print("Cantidad de veces que aparece la letra O: ", vocales[3])
print("Cantidad de veces que aparece la letra U: ", vocales[4])