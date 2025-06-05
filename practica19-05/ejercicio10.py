# Se desea construir una lista llamada productos, en la que cada elemento
# contenga los datos de un producto de un comercio: nombre del producto,
# precio del producto, cantidad disponible, rubro al que pertenece (ej. limpieza, almacén,
# bebidas). Crear una lista con tres productos distintos y mostrar por pantalla:
# a) toda la lista productos,
# b) el nombre y precio del segundo producto,
# c) el stock del primer producto
# d) la categoría del tercer producto.

productos = []
productos.append({"Nombre del producto" : "Lavandina",
                "Precio" : 1500,
                "Cantidad disponible" : 20,
                "Rubro" : "Limpieza"})
productos.append({"Nombre del producto" : "Doritos",
                "Precio" : 2300,
                "Cantidad disponible" : 45,
                "Rubro" : "Almacén"})
productos.append({"Nombre del producto" : "Cerveza",
                "Precio" : 3200,
                "Cantidad disponible" : 154,
                "Rubro" : "Bebidas"})

print("Los productos que tenemos son: ", productos)
print("El segundo producto,", productos[1]["Nombre del producto"],
      " cuesta: $", productos[1]["Precio"])

print("Tenemos", productos[0]["Cantidad disponible"],
      "de ", productos[0]["Nombre del producto"])

print("El producto", productos[2]["Nombre del producto"],
      "pertenece a la categoría de ", productos[2]["Rubro"])