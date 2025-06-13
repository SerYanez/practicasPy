# crear una función que pida al usuario una contraseña dos veces y verifique
# si coinciden.
# Debe manejar excepciones en caso de que el usuario presione Enter sin
# ingresar nada.

def validacion_pass():
    contra = input("Ingrese su contraseña: ").strip()
    contra_2 = input("Ingrese la contraseña nuevamente: ").strip()
    if contra != "" and contra_2 != "":
            if contra == contra_2:
                print("Las contraseñas coinciden.")
            else:
                print("Las contraseñas no coinciden!")
    else:
        print("Contraseña inválida, no puede estar vacía.")

validacion_pass()