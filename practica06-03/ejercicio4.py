# pedir al usuario que ingrese un gasto por día durante 7 días. Al finalizar:
#
# Mostrar el gasto total
#
# Indicar qué día gastó más
#
# Indicar si superó un presupuesto de $10.000

def dia_max_gasto():
    for dia, monto in gastos_semana.items():
            if monto == gasto_max:
                return dia

gastos_semana = {"Lunes": 0.0, "Martes" : 0.0,"Miércoles": 0.0, "Jueves" : 0.0,"Viernes": 0.0,
                 "Sábado" : 0.0,"Domingo" : 0.0}

lunes = float(input("Ingrese el gasto del día lunes: $"))
gastos_semana["Lunes"] = lunes
martes = float(input("Ingrese el gasto del día martes: $"))
gastos_semana["Martes"] = martes
miercoles = float(input("Ingrese el gasto del día miércoles: $"))
gastos_semana["Miércoles"] = miercoles
jueves = float(input("Ingrese el gasto del día jueves: $"))
gastos_semana["Jueves"] = jueves
viernes = float(input("Ingrese el gasto del día viernes: $"))
gastos_semana["Viernes"] = viernes
sabado = float(input("Ingrese el gasto del día sábado: $"))
gastos_semana["Sábado"] = sabado
domingo = float(input("Ingrese el gasto del día domingo: $"))
gastos_semana["Domingo"] = domingo

montos = gastos_semana.values()
total = sum(montos)
gasto_max = max(montos)

print("El gasto total es de: ", total)
print(f"El día de mayor gasto fue el {dia_max_gasto()}, cuando se gastó ${gasto_max}")
if not total >= 10000:
    print("Se mantuvo dentro del presupuesto.")
else:
    print("Se superó el presupuesto de $10,000.")