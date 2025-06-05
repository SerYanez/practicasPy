# Se tienen 3 tuplas con ingredientes que utilizan tres chefs, escribir el
# pseudocódigo y desarrollar un programa que permita mostrar los ingredientes
# que tienen en común los tres, y los ingredientes únicos de cada uno:
chef1 = ("sal", "pimienta", "ajo")
chef2 = ("ajo", "cebolla", "sal")
chef3 = ("pimienta", "limón", "ajo")

chef1_s= set(chef1)
chef2_s= set(chef2)
chef3_s= set(chef3)

ingredientes_comun = chef1_s & chef2_s & chef3_s
print("Ingredientes en común: ", ingredientes_comun)

ingredientes_chef1 = chef1_s - chef2_s - chef3_s
print("Ingredientes únicos del chef 1 son: ", tuple(ingredientes_chef1))

ingredientes_chef2 = chef2_s - chef1_s - chef3_s
print("Ingredientes únicos del chef 2 son: ", tuple(ingredientes_chef2))

ingredientes_chef3 = chef3_s - chef1_s - chef2_s
print("Ingredientes únicos del chef 3 son: ", tuple(ingredientes_chef3))

