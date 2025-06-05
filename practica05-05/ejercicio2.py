#Crea una lista y guardar en ella 5 cadenas de caracteres ingresadas por
#teclado.

frases = []

frases.append(input("Ingresa una frase: "))
frases.append(input("Ingresa una frase: "))
frases.append(input("Ingresa una frase: "))
frases.append(input("Ingresa una frase: "))
frases.append(input("Ingresa una frase: "))

print(frases)

#a) Realizar una copia de la lista y luego invertir sus elementos, y mostrar sus
#elementos por la pantalla

copia_frases = frases.copy()
copia_frases.reverse()
print(copia_frases)

