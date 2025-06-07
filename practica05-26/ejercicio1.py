# Diseñar un algoritmo e implementar el código en Python donde se solicite al
# usuario ingresar un número entero y determine si es positivo, negativo o cero.
# Mostrar un mensaje por pantalla indicando el resultado.

# INGRESAR un número entero
# CALCULAR
#   SI es positivo
#       MOSTRAR mensaje de "Es positivo"
#   SI es negativo
#       MOSTRAR mensaje de "Es negativo"
#   SI es cero
#       Mostrar mensaje de "Es cero"

entero_input = input("Ingrese un número entero: ").strip()
if entero_input.isdigit() > 0 :
    print("El número es positivo")
elif entero_input.isdigit() < 0 :
    print("El número es negativo")
elif entero_input.isdigit() == 0 :
    print("El número es 0")