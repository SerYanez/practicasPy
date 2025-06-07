# Implementar una función llamada mostrar_matriz_como_tabla(matriz_numerica) que reciba como parámetro
# una lista anidada (es decir, una matriz) compuesta por números enteros y/o flotantes y la imprima en
# pantalla formateada como una tabla, donde cada fila esté en una línea separada. Restricción: no se
# debe utilizar librerías externas, solo impresión con print().
# Ejemplo de matriz:
matriz = [[10.5, 200, 3],
          [4, 50.65, 600],
          [70.8, 8, 90]]

def mostrar_matriz_como_tabla(matriz_numerica):
    for i in matriz_numerica:
        for j in i:
            print(f"{j}", end="|")
        print()

mostrar_matriz_como_tabla(matriz)