# Crear una función agregar_producto(nombre, precio) que guarde los productos en un diccionario,
# donde la clave sea el nombre y el valor una tupla (precio, stock). Con otra función recorrer
# el diccionario y mostrar solo los productos con stock mayor a 0.

productos = {}

def agregar_producto(nombre, precio, stock):
    if stock >=0:
        productos[nombre] = (precio, stock)
    else:
        print("Error, el stock no puede ser negativo")

def con_stock(productos):
    for nombre, (precio, stock) in productos.items():
        if not stock == 0:
            print(nombre)

nombre = input("Ingrese el nombre de un producto: ")
precio_input = float(input("Ingrese el precio del producto: "))
stock_input = int(input("Ingrese el stock del producto: "))

agregar_producto(nombre, precio_input, stock_input)
con_stock(productos)