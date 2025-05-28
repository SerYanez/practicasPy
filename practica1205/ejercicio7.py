#Tres artículos tienen listas de palabras clave. Mostrar:
#a. Palabras que aparecen en al menos dos artículos.
#b. Palabras exclusivas de solo uno.
art1 = ["inteligencia", "artificial", "datos"]
art2 = ["datos", "aprendizaje", "modelo"]
art3 = ["modelo", "patrones", "datos"]

art1_s = set(art1)
art2_s = set(art2)
art3_s = set(art3)

interseccion_1y2 = art1_s & art2_s
interseccion_1y3 = art1_s & art3_s
interseccion_2y3 = art2_s & art3_s

palabras_comun = interseccion_1y2 | interseccion_1y3 | interseccion_2y3
print("Palabras que aparecen en al menos 2 conjuntos: ", palabras_comun)

art1_unico = art1_s - art2_s - art3_s
print("La/s palabra/s exclusivas de art1: ", art1_unico)

art2_unico = art2_s - art1_s - art3_s
print("La/s palabra/s exclusivas de art2: ", art2_unico)

art3_unico = art3_s - art1_s - art2_s
print("La/s palabra/s exclusivas de art3: ", art3_unico)