#Tres centros logísticos registran en tuplas los productos enviados. Unificar todos
#los productos, eliminando duplicados, y mostrar cuántos productos únicos hay y
#sus nombres ordenados.
centro1 = ("leche", "pan", "queso")
centro2 = ("pan", "aceite", "harina")
centro3 = ("queso", "fideos", "harina")

conjunto_productos = sorted(set(centro1 + centro2 + centro3))

print("Hay ",len(conjunto_productos), " productos únicos")
print("Los productos son: ", conjunto_productos)