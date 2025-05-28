vector_a = [int(input("Ingrese el primer nro del vector A: ")),
            int(input("Ingrese el segundo nro del vector A: ")),
            int(input("Ingrese el tercer nro del vector A: "))]

vector_b = [int(input("Ingrese el primer nro del vector B: ")),
            int(input("Ingrese el segundo nro del vector B: ")),
            int(input("Ingrese el tercer nro del vector B: "))]

producto_escalar = vector_a [0] * vector_b [0] + vector_a [1] * vector_b [1] + vector_a [2] * vector_b [2]

print(producto_escalar)