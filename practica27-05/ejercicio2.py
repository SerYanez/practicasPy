# Ejercicio 2: dada la estructura a continuación, mostrar las personas mayores de edad que
# viven en Bahía blanca.

personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Bahia Blanca"},
    {"nombre": "Luis", "edad": 17, "ciudad": "Cordoba"},
    {"nombre": "Sofía", "edad": 30, "ciudad": "Bahia Blanca"},
    {"nombre": "Carlos", "edad": 15, "ciudad": "Rosario"}
]

for persona in personas :
    if persona["edad"] >= 18 and persona["ciudad"] == "Bahia Blanca" :
        print(f"{persona["nombre"]} es mayor, y vive en {persona["ciudad"]}")