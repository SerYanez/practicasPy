# Dada una tupla con una secuencia de bases nitrogenadas ("A", "T", "C", "G"),
# convertirla a lista, reemplazar una base, y luego mostrar las bases presentes
# sin repetir. Previamente, escribir el pseudocódigo.
# A: adenina, T: timina, C: citocina, G: guanina, bases que forman el ADN
secuencia = ("A", "T", "C", "G", "A", "G", "T")
secuencia_ls = list(secuencia)
secuencia_ls [0] = "X"
secuencia_mod = set(secuencia_ls)

print(secuencia_mod)
