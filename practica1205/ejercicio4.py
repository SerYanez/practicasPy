# Se tiene una lista de combinaciones de seguridad representadas como tuplas
# (número, letra), eliminar duplicados y verificar si una combinación dada por el
# usuario está entre las válidas.
combinaciones = [(1, 'A'), (2, 'B'), (1, 'A'), (3, 'C')]
combinacion_usuario = (2, 'B')

combinaciones_unicas = set(combinaciones)
print(combinaciones_unicas)
v_o_f = combinacion_usuario in combinaciones_unicas
print("La combinación es válida? ", v_o_f)