# 1- Crear un diccionario llamado producto con las claves: nombre, precio,
# stock.
# a- Agregar una nueva clave llamada categoría y luego mostrar todas las
# claves,
# b- Ingresar un valor para cada clave desde teclado, convirtiendo el dato al
# tipo que sea más factible.


producto = {"Nombre" : "", "Precio" : 0.0, "Stock" : 1}
producto ['Categoría'] = ""
print(producto.keys())
print("Agregue valores correspondientes a cada campo")
nombre = input("Nombre del producto: ")
precio = input("Precio del producto: ")
stock = input("Cantidad en stock: ")
categoria = input("Categoría de clasificación: ")

producto["Nombre"] = nombre
producto["Precio"] = precio
producto["Stock"] = stock
producto["Categoria"] = categoria

print("Producto agregado! Detalles: ", producto)