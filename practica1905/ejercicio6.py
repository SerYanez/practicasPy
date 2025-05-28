# 6- Crear un diccionario empleados donde las claves sean nombres y los
# valores sean sets con habilidades. Verificar si "python" está entre las
# habilidades de uno de ellos.

empleados = {}
empleados["Jorge"] = {"logística", "comunicación"}
empleados["Luis"] = {"administración", "logística",}
empleados["Pablo"] = {"ventas", "comunicación"}
empleados["Juan"] = {"python", "administración"}
empleados["Santiago"] = {"logística", "comunicación"}

verificacion_jorge = "python" in empleados["Jorge"]
verificacion_luis = "python" in empleados["Luis"]
verificacion_pablo = "python" in empleados["Pablo"]
verificacion_juan = "python" in empleados["Juan"]
verificacion_santiago = "python" in empleados["Santiago"]
verificacion_final = (verificacion_jorge | verificacion_luis | verificacion_pablo
                      | verificacion_juan | verificacion_santiago)

print("Algún empleado maneja python? ", verificacion_final)