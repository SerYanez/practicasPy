# Escribir una función que reciba una temperatura en °C y la convierta a °F.
# Luego, usar esa función para convertir un conjunto de temperaturas
# (por ejemplo: [18, 22, 30, 12]) y mostrar
# si alguna supera los 85 °F.
#
# fahrenheit = celsius * 9/5 + 32

def convertir_a_f(celsius):
    farenheit = celsius * 9/5 +32
    return farenheit

def convertir_lista(lista_1, lista_2):
    for i in lista_1:
        lista_2.append(convertir_a_f(i))

def advertencia(lista):
    alerta = False
    for i in lista:
        if i > 85:
            alerta = True
    return alerta

temps_c = [18, 22, 30, 12]
temps_f = []

convertir_lista(temps_c, temps_f)
if advertencia(temps_f):
    print("Hay temperaturas sobre los 85°F!")
