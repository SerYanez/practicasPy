notas = []

notas.append(float(input("Ingrese la nota nro1 (0-10): ")))
notas.append(float(input("Ingrese la nota nro1 (0-10): ")))
notas.append(float(input("Ingrese la nota nro1 (0-10): ")))
notas.append(float(input("Ingrese la nota nro1 (0-10): ")))
notas.append(float(input("Ingrese la nota nro1 (0-10): ")))

nota_alta = max(notas)
nota_baja = min(notas)
nota_promedio = sum(notas) / len(notas)

print(f"La nota más alta fue: {nota_alta}" )
print(f"La nota más baja fue: {nota_baja}" )
print(f"La nota promedio es: {nota_promedio}" )