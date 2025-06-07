# pedir que se ingresen 5 nombres y edades. Guardarlos en un diccionario. Luego mostrar:
#
# Quiénes son mayores de edad
#
# El promedio de edades
#
# La persona más joven

def mayores_o_no(personas):
    for nombre, edad in personas.items():
        if edad < 18:
            print(f"-{nombre} es menor de edad.")
        elif edad >= 18:
            print(f"-{nombre} es mayor de edad")

def promedio_edades(personas):
    edades = personas.values()
    total_edades = sum(edades)
    return total_edades / len(edades)

def promedio_2(personas):
    total = 0
    for nombre, edad in personas.items():
        total += edad
    return total

def edad_min(personas):
    edades = personas.values()
    menor_edad = min(edades)
    for nombre, edad in personas.items():
        if edad == menor_edad:
            return nombre

personas = {}

print("Ingrese nombres y edades de 5 personas")
nombre_1 = input("Ingrese el nombre de la persona 1: ")
edad_1 = int(input("Ingrese la edad de la persona 1: "))
personas[nombre_1] = edad_1
nombre_2 = input("Ingrese el nombre de la persona 2: ")
edad_2 = int(input("Ingrese la edad de la persona 2: "))
personas[nombre_2] = edad_2
nombre_3 = input("Ingrese el nombre de la persona 3: ")
edad_3 = int(input("Ingrese la edad de la persona 3: "))
personas[nombre_3] = edad_3
nombre_4 = input("Ingrese el nombre de la persona 4: ")
edad_4 = int(input("Ingrese la edad de la persona 4: "))
personas[nombre_4] = edad_4
nombre_5 = input("Ingrese el nombre de la persona 5: ")
edad_5 = int(input("Ingrese la edad de la persona 5: "))
personas[nombre_5] = edad_5

print("De la lista de personas: ")
mayores_o_no(personas)

print(f"El promedio de edades es: {promedio_edades(personas)}")
#print(f"El promedio de edades es: {promedio_2(personas)}")

print(f"La persona más joven es: {edad_min(personas)}")

