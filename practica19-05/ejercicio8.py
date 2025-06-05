# Crear un diccionario colores con claves de tipo frozenset para representar
# mezclas de colores: por ejemplo, frozenset({"rojo", "azul"}) → "violeta".
# Consultar en internet una mezcla específica.

colores = {frozenset({"rojo", "azul"}): "violeta",
           frozenset({"rojo", "amarillo"}): "naranja",
           frozenset({"azul", "amarillo"}): "verde",
           frozenset({"blanco", "negro"}): "gris",
           }

mezcla = frozenset({"amarillo", "azul"})
color_resultante = colores[mezcla]

print("El resultado de", mezcla, "es:", color_resultante )