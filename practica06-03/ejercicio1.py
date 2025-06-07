# pedir al usuario su edad y género. Validar que la edad sea un número positivo y que el
# género sea "M", "F", "Otro". Mostrar un mensaje personalizado, por ejemplo:
# "Bienvenido, usuario masculino de 25 años."

def edad_usuario(edad):
        if edad.strip().isdigit() > 0:
            return edad
        else:
            print("Edad no válida")
            return False

def genero_usuario(genero):
    if genero.strip().lower() in ["m", "f", "o"]:
        return genero.strip().lower()
    print("Género no válido")
    return False

while True:
    edad = input("Ingrese su edad: ")
    edad_elegida = edad_usuario(edad)
    if edad_elegida:
        break
while True:
    genero = input("Ingrese su género (M/F/O): ")
    gen_elegido = genero_usuario(genero)
    if gen_elegido:
        break

if gen_elegido == "f":
    print(f"Bienvenido usuario femenino, {edad_elegida} años")

elif gen_elegido == "m":
    print(f"Bienvenido usuario masculino, {edad_elegida} años")

elif gen_elegido == "o":
    print(f"Bienvenido usuario otro, {edad_elegida} años")



