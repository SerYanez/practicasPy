# Pedir al usuario 10 números y contar cuántos son pares. Validar cada entrada
# con try-except. Mostrar resultados al final con una función.

def pares(lista_nros):
    pares = [num for num in lista_nros if num % 2 == 0]
    print(f"La cantidad de números pares en la lista es de: {len(pares)}")
    print("Los números pares de la lista son: ")
    for i in pares:
            print(i, end= " ")


lista_numeros = []
while 10 > len(lista_numeros):
    try:
        nro = int(input("Ingrese un número: "))
        lista_numeros.append(nro)
    except ValueError:
        print("Número inválido")

pares(lista_numeros)
