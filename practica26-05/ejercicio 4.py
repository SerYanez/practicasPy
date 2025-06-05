# Diseñar un algoritmo e implementarlo en Python que recorra los números del 1 al
# 50 utilizando un bucle. Durante el recorrido, se debe verificar si cada número es
# múltiplo de 3, de 5 o de ambos. Para los múltiplos de 3 se debe mostrar el
# mensaje "Fizz", para los múltiplos de 5 el mensaje "Buzz" y para los que sean
# múltiplos de ambos, el mensaje "FizzBuzz". En los demás casos, se debe mostrar
# el número.

''' Pseudocódigo

    POR cada número en un rango de 1 a 50
        SI el nro es múltiplo de 3 y 5
            MOSTRAR nro + FizzBuzz
        SI el nro es múltiplo de 5
            MOSTRAR nro + Buzz
        SI el nro el múltiplo de 3
            MOSTRAR nro + Fizz
'''

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)