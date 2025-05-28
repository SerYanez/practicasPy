#pido que el usuario ingrese la temperatura actual
temp = int(input("Cuál es la temperatura ambiente en Celsius? "))

#condicional para advertir por temperaturas peligrosas (más de 30 y menos de 0)
if temp >= 50 or -20 >= temp :
    print("¡¡ALERTA ROJA!!")
elif 40 <= temp < 50 or -10 >= temp > -20:
    print("ALERTA NARANJA!")
elif 30 <= temp < 40 or 0 > temp > -10:
    print("Alerta amarilla")
else:
    print("La temperatura es agradable")