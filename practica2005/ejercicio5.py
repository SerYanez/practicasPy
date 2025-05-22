#usuario ingresa un ángulo, se guarda en una variable
ang = int(input("Ingrese un ángulo (sólo números): "))

#se calcula qué tipo de ángulo es

if ang == 0 :
    print("El ángulo es nulo")
elif 0 < ang < 90 :
    print("El ángulo es agudo")
elif ang == 90 :
    print("El ángulo es recto")
elif 90 < ang < 180 :
    print("El ángulo es obtuso")
elif ang == 180 :
    print("El ángulo es llano")
elif 180 < ang < 360 :
    print("El ángulo es cóncavo")
elif ang == 360 :
    print("El ángulo es completo")
else:
    print("El ángulo es inválido")