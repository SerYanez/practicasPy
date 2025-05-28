# Las siguientes listas representan los elementos químicos involucrados en tres
# reacciones químicas diferentes:
reaccion1 = ["H", "O", "Cl"]
reaccion2 = ["O", "H"]
reaccion3 = ["N", "Cl", "O"]
# a- Plantear el pseudocódigo,
# b- Verificar si en una reacción hay un subconjunto de otra.

# Convertir las listas a conjuntos para poder comparar
conjunto_r1 = set(reaccion1)
conjunto_r2 = set(reaccion2)
conjunto_r3 = set(reaccion3)

# Comparar subconjuntos
print("¿Reacción 1 es subconjunto de Reacción 2?:", conjunto_r1.issubset(conjunto_r2))
print("¿Reacción 1 es subconjunto de Reacción 3?:", conjunto_r1.issubset(conjunto_r3))
print("¿Reacción 2 es subconjunto de Reacción 1?:", conjunto_r2.issubset(conjunto_r1))
print("¿Reacción 2 es subconjunto de Reacción 3?:", conjunto_r2.issubset(conjunto_r3))
print("¿Reacción 3 es subconjunto de Reacción 1?:", conjunto_r3.issubset(conjunto_r1))
print("¿Reacción 3 es subconjunto de Reacción 2?:", conjunto_r3.issubset(conjunto_r2))