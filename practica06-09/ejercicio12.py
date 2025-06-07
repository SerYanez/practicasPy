# Crear una función que calcule la raíz cuadrada de un número. Validar que el
# número sea positivo. Si es negativo, mostrar mensaje de error.

def raiz(nro):
    try:
        num = float(nro)
        if num >= 0:
            raiz = num ** 0.5
            return raiz
        else:
            print("Número debe ser positivo")
    except ValueError:
        return "Número inválido"

num = input("ingrese un número para calcular su raíz cuadrada: ")
print(raiz(num))